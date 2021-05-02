import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib import parse,

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')
        print(self.path)
        if self.path == "/":
            contents = Path('form-1.html').read_text()
        elif self.path.startswith("/echo?msg"):
            message = parse_qs(urlparse(self.path).query)["msg"][0] #this will create a dict with the key: msg and a value:a list of what is in the msg
            contents = Path("/template.html").read_text().format(message)

        else:
            contents = Path("/error.html").read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return


# - Server MAIN program
Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()