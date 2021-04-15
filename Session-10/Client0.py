import termcolor
import colorama
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
        colorama.init(strip="False")
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print(termcolor.colored("To server:" + msg, "yellow"))
        s.send(msg.encode()) #another way of doing it is: s.send(str.encode(msg))
        # Receive data
        response = s.recv(2048).decode("utf-8")
        print(termcolor.colored("From server:" + msg, "blue"))
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response


