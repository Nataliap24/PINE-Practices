from Client0 import Client

print(" Paractice 2, ex3")

IP = "127.0.0.1"
PORT = 10000
c = Client(IP, PORT)
response = c.talk("message")
print("Response:", response)