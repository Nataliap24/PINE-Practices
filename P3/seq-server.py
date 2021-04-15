import socket
import server_utils

list_sequences = ["AAGCTGCTACGTACGTACAGCT", "ACGGATCGCATCGATCGTACGATCGATCATC", "CGATAGCTGATCGATCATGCTACGTGTACG", "AGTAGCTAGTGCTACGATTATCGATCA", "CAGTCGATCGATTACG"]


PORT = 8080
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
client_adress_list = []
print("The server is configured!")

while True:

    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_adress_list.append(client_ip_port)
        print("CONNECTION ESTABLISHED. Client IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    formatted_message = server_utils.format_command(msg)
    formatted_message = formatted_message.split(" ")

    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
        command = formatted_message[0]
        argument = formatted_message[1]

    if command == "PING":
        server_utils.ping(cs)
    elif command == "GET":
        server_utils.get(cs, list_sequences, argument)
    elif command == "INFO":
        server_utils.info(cs, argument)
    elif command == "COMP":
        server_utils.comp(cs, argument)
    elif command == "REV":
        server_utils.rev(cs, argument)
    elif command == "GENE":
        server_utils.gene(cs, argument)
    else:
        response = "Not available command"
        cs.send(response.encode())

    ls.close()

#echo 2 | nc -w 1 127.0.0.1 8080