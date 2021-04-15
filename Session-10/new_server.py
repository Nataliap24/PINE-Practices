import socket

# Configure the Server's IP and PORT of the machine where the server is running (our computer)
PORT = 8080
IP = "127.0.0.1"
# -- Step 1: create the socket (Method socket())
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# -- Step 2: Bind the socket to server's IP and PORT (Method bind()
ls.bind((IP, PORT))
count_connections = 0
# -- Step 3: Configure the socket for listening (Method listen())
ls.listen()
client_adress_list = []
print("The server is configured!")

while True:

    #Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_adress_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION" + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))

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

        #Send a response message to the client with integer messages
        response = "ECHO" + msg
        # -- The message has to be encoded into bytes
        cs.send(response.encode())


        # -- Close the socket
        ls.close()
        if count_connections == 5:
            for i in range(0, len(client_adress_list)):
                print("Client" + str(i) + ":Client IP, PORT: " + str(client_adress_list[i]))
            exit()