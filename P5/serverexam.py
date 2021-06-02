#IT IS THE SAME AS SERVER.PY BUT WITHOUT COLOURS
import http.server
import socketserver
import pathlib
import json

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)
        print(self.path)  # to avoid splitting

        if self.path == "/":
            content_type = 'text/html'
            contents = read_html_file("./html/index.html")
        elif self.path == "/info/A":
            content_type = 'application/json'
            answer = {'Name': 'Adenine', 'Letter': 'A', 'Link': 'https://en.wikipedia.org/wiki/Adenine',
                      'Formula': 'C5H5N5'}
            contents = json.dumps(answer)
        elif self.path == "/info/C":
            content_type = 'text/html'
            contents = read_html_file("./html/info/C.html")
        elif self.path == "/info/G":
            content_type = 'text/html'
            contents = read_html_file("./html/info/G.html")
        elif self.path == "/info/T":
            content_type = 'text/html'
            contents = read_html_file("./html/info/T.html")
        elif self.path.endswith(".html"):
            content_type = 'text/html'
            try:
                contents = read_html_file("./html" + self.path)
            except FileNotFoundError:
                contents = read_html_file("./html/error.html")
        else:
            content_type = 'text/html'
            contents = read_html_file("./html/error.html")

        # Generating the response message
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(contents.encode())
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()