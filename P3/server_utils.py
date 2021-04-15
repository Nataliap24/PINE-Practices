from Seq1 import Seq
GENE_FOLDER = "../P0/Sequences/"

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command): #this is bc if we try to send "PING", we get PING\r\n
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command", "green")
    response = "OK"
    cs.send(response.encode())

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())

def info(cs, argument): #argument = sequence
    print_colored("INFO", "yellow")
    seq = Seq(argument)
    length = "Total length: " + str(seq.len())
    count = seq.count_bases() #tuple with number of bases
    suma = count[0] + count[1] + count[2] + count[3]
    response = length + "\n"
    for i in range(0, len(count)):
        list_bases = ["A: ", "C: ", "G: ", "T: "]
        percentage = str(round((count[i] / suma) * 100, 2)) + "%"
        response += list_bases[i] + str(count[i]) + " -->  " + percentage + "\n"
    cs.send(response.encode())
    print(response)

def comp(cs, argument):
    print_colored("COMP", "yellow")
    seq = Seq(argument)
    complement = seq.complement()
    cs.send(complement.encode())
    print(complement)

def rev(cs, argument):
    print_colored("REV", "yellow")
    seq = Seq(argument)
    reverse = seq.reverse()
    cs.send(reverse.encode())
    print(reverse)

def gene(cs, argument): #argument = gene name
    try:
        print_colored("GENE", "yellow")
        seq = Seq()
        seq.read_fasta(GENE_FOLDER + argument + ".txt")
        cs.send(str(seq).encode())
        print(seq)
    except FileNotFoundError:
        cs.send("There´s no such file".encode())



