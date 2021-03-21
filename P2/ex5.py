from Client0 import Client
from pathlib import Path

print(" Paractice 2, ex5")

IP = "127.0.0.1"
PORT = 10000
c = Client(IP, PORT)
response = c.talk("message")
print(c.talk("sending the U5 gene to the server"))
print(c.talk(Path("U5.txt").read_text()))


