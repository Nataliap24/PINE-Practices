import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8080
IP = "192.168.124.179"


# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #we need a socket method that will return that it is a socket (we just create a socket)
                                                      #socket.AD_INET is the default socket
                                                      #socket.socket_stream is a statement that tells the program that we are going to use a TCT? socket

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT)) #(IP, PORT) needs to be a tupple

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048) #this number just tells python what is used to store the info
print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))

# Closing the socket
s.close()