from Client0 import Client
from pathlib import Path
from Seq1 import Seq

print(" Paractice 2, ex6")

IP = "127.0.0.1"
PORT = 10000
PORT2 = 12500

c = Client(IP, PORT)
c_2 = Client(IP, PORT2)
s = Seq()
s.read_fasta('../P0/Sequences/FRAT1.txt')
count = 0
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i: i + 10]
    count += 1
    i += 10
    print("Frangment", count, ":", fragment)
    if count % 2 == 0:
        print(c_2.talk("Frangment " + str(count) + ": " + fragment))
    else:
        print(c.talk("Frangment " + str(count) + ": " + fragment))