from Clientclass import Client

PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)
command = input("Enter a command: ")
if command == "INFO" or command == "COMP" or command == "REV":
    print("* Testing", command, "...")
    c.talk(command + " AAGCTGCTACGTACGTACAGCT")
else:
    exit = True
    while exit:
        argument = input("Introduce a proper argument (or press enter for PING): ")
        if len(argument) == 0 and command != "PING":
            print("You need to introduce an argument. The only command with no argument is PING")
        else:
            print("* Testing", command, "...")
            c.talk(command + " " + argument)
            exit = False

