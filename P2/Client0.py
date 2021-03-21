import termcolor
import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self): #the ping worked with a url in the console
        print("OK")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #if we try to connect a socket to sthg that is not running we get an exception
        try:
            s.connect((self.ip, self.port)) #in the connect function we need a tuple of the ip and the port
            print("The server is up")
        except ConnectionRefusedError:
            print("Could not connect to the server")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        #print("To server:", msg)
        s.send(str.encode(msg))
        # Receive data
        response = s.recv(2048).decode("utf-8")
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response
    def debug_talk(self, msg, resp):
        termcolor.cprint("To server: " + msg, 'blue')
        termcolor.cprint(resp, 'green')

