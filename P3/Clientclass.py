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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print(termcolor.colored(msg, "green"))
        s.send(msg.encode())
        response = s.recv(2048).decode("utf-8")
        print(termcolor.colored(response, "blue"))
        s.close()
        return "From server: " + response

