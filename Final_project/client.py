import http.client
import json



IP = 'localhost'
PORT = 8080
print(f"\nConnecting to server: {IP}:{PORT}\n")
conn = http.client.HTTPConnection(IP, PORT)

try:
    conn.request("GET", "/species?limit=10&json=1")
    r1 = conn.getresponse().read().decode("utf-8")
    dict_r1 = json.loads(r1)
    print("LIST SPECIES:", dict_r1)

    conn.request("GET", "/karyotype?specie=human&json=1")
    r2 = conn.getresponse().read().decode("utf-8")
    dict_r2 = json.loads(r2)
    print("KARYOTYPE:", dict_r2)

    conn.request("GET", "/chromosomeLenght?specie=human&chrom=X&json=1")
    r3 = conn.getresponse().read().decode("utf-8")
    dict_r3 = json.loads(r3)
    print("CHROMOSOME LENGTH:", dict_r3)

    conn.request("GET", "/seq?gene=FRAT1&json=1")
    r4 = conn.getresponse().read().decode("utf-8")
    dict_r4 = json.loads(r4)
    print("SEQUENCE:", dict_r4)

    conn.request("GET", "/info?gene=FRAT1&json=1")
    r5 = conn.getresponse().read().decode("utf-8")
    dict_r5 = json.loads(r5)
    print("GENE INFORMATION:", dict_r5)

    conn.request("GET", "/calc?gene=FRAT1&json=1")
    r6 = conn.getresponse().read().decode("utf-8")
    dict_r6 = json.loads(r6)
    print("GENE CALCULATIONS:", dict_r6)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

