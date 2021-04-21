#URL links have parameters ex: http://127.0.0.1:8080/hi/there?name=virus&type=corona -> the part after the question mark is the parameter
#they are variable names with their values
#when we try to call our server (basis of ex6 server) with that we get an error bc it does not know it is a parameter
#we will modify this server so it can read it

import socket
import termcolor
import pathlib
from urllib.parse import urlparse, parse_qs

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()
    print("Message FROM CLIENT: ")
    lines = req.split('\n')
    req_line = lines[0]
    request = req_line.split(" ")[1]#after splitting we will have in one part the pathname and in the other one everything that comes after the question mark
    print("Request:", request) #in the request we will get an error bc /favicon.ico is inclueded and it can´t be read? so we need to put a try
    path_name = request.split("?")[0]
    print("Resource requested:", path_name)
    try:
        parameters = request.split("?")[1]
        print("Arguments:", parameters)
        # in parameters we will get name=virus&type=corona and we need to get the variables and values from there
        # we are going to use the urlpase library to solve it
        # these functions divide the string in two parts.
        o = urlparse(req_line.split(" ")[1])
        query = parse_qs(o.query)
        print(o)
        print(query)
    except IndexError:
        pass
    """
    having the urlpase library we could have just written
    lines = req.split('\n')
    req_line = lines[0]
    request = req_line.split(" ")[1]
    o = urlparse(request)
    path_name = o.path
    arguments = parse_qs(o.query)
    ---> if we write in our url .../A?name=Adenosine , we get in the parameters {'name':[Adenosine]{
    """



    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"

    if path_name == "/":
        body = read_html_file("./html/index.html")
    elif "/info/" in path_name:
        try:
            body = read_html_file("./html/" + path_name.split('/')[-1] + ".html")
        except FileNotFoundError:
            body = read_html_file("./html/error.html")
    else:
        body = read_html_file("./html/error.html")

    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())
    # in html files <br> is the end of line character (para la siguiente linea),
    # so if we wanted the "main page" ,message to be printed in the next line we would have to add it next to the previous line
    #instead of <br> we can write <p></p> under the previous line


# ------ Configure the server
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("SEQ Server configured!")
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()