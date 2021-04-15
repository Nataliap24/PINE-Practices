import socket

# Configure the Server's IP and PORT of the machine where the server is running (our computer)
PORT = 8080
IP = "192.168.1.118" #if we write "localhost" instead of the ip, it will work but only for the clients in our computer
                    #if we leave it empty ("") we tell the system to listen to all the ip adresses in the machine

# -- Step 1: create the socket (Method socket())
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT (Method bind()
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening (Method listen())
ls.listen()

print("The server is configured!")

while True:

    #Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept() #cs is a port and client_ip_port is a tuple with the ip and the port of the cñient
        print("A client has connected to the server!")

    # -- Server stopped manually
    except KeyboardInterrupt: #if we print ctrl+c the server will be closed manually (this does not work as it should in windows)
        print("Server stopped by the user")
        # -- Close the listenning socket
        ls.close()
        # -- Exit!
        exit()

    else:
        #Read the message from the client
        # READ THE MESSAGE FROM THE CLIENT
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)
        # -- We decode it for converting it into a human-redeable string
        msg = msg_raw.decode()
        # -- Print the received message
        print(f"Received Message: {msg}")

        #Send a response message to the client
        response = "HELLO. I am the Happy Server :-)\n"
        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the socket
        ls.close()