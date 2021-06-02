import http.client
import json
import Seq1

DICT_GENES = {
    "FRAT 1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)

try:  #en el examen puede preguntar como hacer esto pero para todos (sin el input, con un for)
    user_gene = input("Enter the Gene that you want to analyse: ")
    id = DICT_GENES[user_gene]
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        #print(json.dumps(response_dict, indent=4, sort_keys=True))  #this is to print the dict
        sequence = Seq1.Seq(response_dict["seq"])
        s_length = sequence.len()
        per = sequence.percentage()
        print("Total length:", s_length)
        print("The percentages are:")
        for e in per:
         print(e)

except KeyError:
    print("The gene is not inside of our dictionary. Choose one pf the following:", list(DICT_GENES.keys()))