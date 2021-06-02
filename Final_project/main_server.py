import http.server
import pathlib
import socketserver
from urllib.parse import urlparse, parse_qs
import server_functions as su

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
GENE_DICT = {
    "FRAT1": "ENSG00000165879",
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


def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)
        print("Path:", self.path)

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)

        if "json" in arguments.keys():
            content_type = 'application/json'
            if path_name == "/species":
                try:
                    if "limit" in arguments.keys():
                        limit = arguments['limit'][0]
                    else:
                        limit = 1000
                    contents = su.species_names_json(limit)
                except ValueError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/karyotype":
                try:
                    specie = arguments["specie"][0].replace(" ", "_")
                    contents = su.karyotype_json(specie)
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/chromosomeLenght":
                try:
                    specie = arguments["specie"][0].replace(" ", "_")
                    chromosome = arguments["chrom"][0]
                    contents = su.length_chrom_json(specie, chromosome)
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/seq":
                try:
                    gene_name = arguments["gene"][0]
                    contents = su.gene_seq_json(gene_name, GENE_DICT[gene_name])
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/info":
                try:
                    gene_name = arguments["gene"][0]
                    contents = su.gene_info_json(gene_name, GENE_DICT[gene_name])
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/calc":
                try:
                    gene_name = arguments["gene"][0]
                    contents = su.gene_calc_json(gene_name, GENE_DICT[gene_name])
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()

        else:
            content_type = 'text/html'
            if path_name == "/":
                contents = su.read_template_html_file("./html/mainpage.html").render()
            elif path_name == "/species":
                try:
                    if "chk" in arguments.keys():
                        print("The checkbox was checked")
                    else:
                        print('The checkbox was not checked')
                    if "limit" in arguments.keys():
                        limit = arguments['limit'][0]
                    else:
                        limit = 1000
                    contents = su.species_names(limit)
                except ValueError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/karyotype":
                try:
                    specie = arguments["specie"][0].replace(" ", "_")
                    contents = su.karyotype(specie)
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/chromosomeLenght":
                try:
                    specie = arguments["specie"][0].replace(" ", "_")
                    chromosome = arguments["chrom"][0]
                    contents = su.length_chrom(specie, chromosome)
                except KeyError or UnboundLocalError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/seq":
                try:
                    gene_name = arguments["gene"][0]
                    contents = su.gene_seq(gene_name, GENE_DICT[gene_name])
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/info":
                try:
                    gene_name = arguments["gene"][0]
                    contents = su.gene_info(gene_name, GENE_DICT[gene_name])
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()
            elif path_name == "/calc":
                try:
                    gene_name = arguments["gene"][0]
                    contents = su.gene_calc(gene_name, GENE_DICT[gene_name])
                except KeyError:
                    contents = su.read_template_html_file("./html/error.html").render()

            else:
                contents = su.read_template_html_file("./html/error.html").render()

        # Generating the response message
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(contents.encode())
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()