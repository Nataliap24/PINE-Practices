import http.server
import socketserver

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler  #The handler is used by the TCP sever to understand the http message

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd: #TCP means that we create a TCP server.
                                                        #it needs a tuple with the port and the ip adress where the server is listening on (when we write "" the servers listens in all ip´s that are in the computer)
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()