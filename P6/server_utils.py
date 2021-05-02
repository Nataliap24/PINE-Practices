from Seq1 import Seq
import pathlib
import jinja2
from urllib.parse import urlparse, parse_qs
GENE_FOLDER = "./Sequences/"

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command): #this is bc if we try to send "PING", we get PING\r\n
    return command.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def ping(cs):
    print_colored("PING command", "green")
    response = "OK"
    cs.send(response.encode())

def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)]
    context = {"number": seq_number, "sequence": sequence}
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents


def info(argument):
    print_colored("INFO", "yellow")
    seq = Seq(argument)
    length = "Total length: " + str(seq.len())
    bases_count = seq.count_bases()[0]
    percentages = seq.count_bases()[1]
    response = [length]
    for i in range(0, len(bases_count)):
        list_bases = ["A: ", "C: ", "G: ", "T: "]
        response.append(list_bases[i] + str(bases_count[i]) + " -->  " + str(percentages[i]) + "%")
    context = {'sequence': argument, 'info_sequence': response}
    contents = read_template_html_file("./html/info.html").render(context=context)
    return contents

def comp(argument):
    print_colored("COMP", "yellow")
    seq = Seq(argument)
    complement = seq.complement()
    context = {"sequence": argument, "comp_sequence": complement}
    contents = read_template_html_file("./html/comp.html").render(context=context)
    return contents

def rev(argument):
    print_colored("REV", "yellow")
    seq = Seq(argument)
    reverse = seq.reverse()
    context = {"sequence": argument, "rev_sequence":reverse}
    contents = read_template_html_file("./html/rev.html").render(context=context)
    return contents

def gene(seq_name):
    print_colored("GENE", "yellow")
    PATH = GENE_FOLDER + seq_name + ".txt"
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {"gene_name": seq_name, "gene_contents": s1.strbases}
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents



