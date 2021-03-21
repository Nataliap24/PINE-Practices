from Client0 import Client

print(" Paractice 2, ex4")

IP = "127.0.0.1"
PORT = 10000
c = Client(IP, PORT)
mes_1 = "Message 1---"
mes_2 = "Message 2---"
c.debug_talk(mes_1, c.talk(mes_1))
c.debug_talk(mes_2, c.talk(mes_2))
