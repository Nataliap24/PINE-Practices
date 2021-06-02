import http.client
import pathlib
import jinja2
import json
from Seq1 import Seq


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def species_names(limit):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/species"
    PARAMETERS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMETERS)
    response = connection.getresponse().read().decode()
    species = json.loads(response)["species"]
    list_species = []
    for dictionary in species:
        list_species.append(dictionary["common_name"])
    num_species = len(list_species)
    context = {"names":list_species[:int(limit)], "number":num_species, "limit":limit}
    contents = read_template_html_file("./html/species.html").render(context=context)
    return contents

def karyotype(species):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/assembly/"
    PARAMETERS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT+ species + PARAMETERS)
    response = connection.getresponse().read().decode()
    list_dict = json.loads(response)['top_level_region']
    list_chrom = []
    for e in list_dict:
        if e['coord_system'] == 'chromosome':
            list_chrom.append(e['name'])
    context = {"list_chrom": list_chrom}
    contents = read_template_html_file("./html/karyotype.html").render(context=context)
    return contents

def length_chrom(specie, chromosome):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/assembly/"
    PARAMETERS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + specie + PARAMETERS)
    response = connection.getresponse().read().decode()
    list_dict = json.loads(response)['top_level_region']
    for e in list_dict:
        if e['coord_system'] == 'chromosome' and e['name']==chromosome:
            context = {"length":e["length"]}
    contents = read_template_html_file("./html/chromlength.html").render(context=context)
    return contents

def gene_seq(gene_name, id):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMETERS = "?content-type=text/plain;species=human"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse().read().decode()
    context = {"gene_name":gene_name, "sequence":response}
    contents = read_template_html_file("./html/geneseq.html").render(context=context)
    return contents

def gene_info(gene_name, id):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMETERS = "?content-type=application/json;species=human"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse().read().decode()
    dict_info = json.loads(response)
    chrom_info = dict_info["desc"].split(":")
    context = {"gene_name":gene_name, "id":id, "chrom_name":chrom_info[1], "start":chrom_info[3], "end":chrom_info[4], "length":len(dict_info['seq'])}
    contents = read_template_html_file("./html/gene_info.html").render(context=context)
    return contents

def gene_calc(gene_name, id):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMETERS = "?content-type=text/plain;species=human"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse().read().decode()
    seq = Seq(response)
    context = {"gene_name": gene_name, "length":str(seq.len()), "percentages":seq.percentage()}
    contents = read_template_html_file("./html/gene_calc.html").render(context=context)
    return contents


#-------------JSON FUNCTIONS--------------------------------

def species_names_json(limit):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/species"
    PARAMETERS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMETERS)
    response = connection.getresponse().read().decode()
    species = json.loads(response)["species"]
    list_species = []
    for dictionary in species:
        list_species.append(dictionary["common_name"])
    num_species = len(list_species)
    contents = {"number":num_species, "limit":limit, "species":list_species[:int(limit)]}
    contents_json = json.dumps(contents)
    #print(contents_json)
    return contents_json

def karyotype_json(species):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/assembly/"
    PARAMETERS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + species + PARAMETERS)
    response = connection.getresponse().read().decode()
    list_dict = json.loads(response)['top_level_region']
    list_chrom = []
    for e in list_dict:
        if e['coord_system'] == 'chromosome':
            list_chrom.append(e['name'])
    contents = {"list_chrom": list_chrom}
    contents_json = json.dumps(contents)
    return contents_json

def length_chrom_json(specie, chromosome):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/info/assembly/"
    PARAMETERS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + specie + PARAMETERS)
    response = connection.getresponse().read().decode()
    list_dict = json.loads(response)['top_level_region']
    for e in list_dict:
        if e['coord_system'] == 'chromosome' and e['name']==chromosome:
            contents = {"length": e["length"]}
    contents_json = json.dumps(contents)
    return contents_json

def gene_seq_json(gene_name, id):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMETERS = "?content-type=text/plain;species=human"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse().read().decode()
    contents = {"gene_name":gene_name, "sequence":response}
    contents_json = json.dumps(contents)
    return contents_json

def gene_info_json(gene_name, id):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMETERS = "?content-type=application/json;species=human"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse().read().decode()
    dict_info = json.loads(response)
    chrom_info = dict_info["desc"].split(":")
    contents = {"gene_name":gene_name, "id":id, "chrom_name":chrom_info[1], "start":chrom_info[3], "end":chrom_info[4], "length":len(dict_info['seq'])}
    contents_json = json.dumps(contents)
    return contents_json

def gene_calc_json(gene_name, id):
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    PARAMETERS = "?content-type=text/plain;species=human"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse().read().decode()
    seq = Seq(response)
    contents = {"gene_name": gene_name, "length":str(seq.len()), "percentages":seq.percentage()}
    contents_json = json.dumps(contents)
    return contents_json