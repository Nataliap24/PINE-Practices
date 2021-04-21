import socket
import termcolor
import pathlib

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
    path_name = req_line.split(" ")[
        1]  # This way we get a list with the path name, path and mode?, and by adding [1] we only get the path name
    termcolor.cprint(req_line, "green")
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