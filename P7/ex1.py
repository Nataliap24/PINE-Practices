import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"   #this is the path of the url to get the thing inside the json
PARAMS = "?content-type=application/json"  #we need to add this so it appears in json format (as a dict)

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)  #the frist parameter is the type of query (GET) and the second one is the path?
response = connection.getresponse()
answer_decoded = response.read().decode()    #the read is bc response is an object. Now we get b'{"ping:1{' , which are bytes, so we need to decode it
dict_response = json.loads(answer_decoded)  #it will be of type dict
if dict_response["ping"] == 1:
    print("PING OK!! the database is running")
else:
    print("Database is down!!")

