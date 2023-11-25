from hds_parser import HDS_Parser

parser = HDS_Parser()

input_file = open("func.show", "r")
input_string = input_file.read()
input_file.close()

python_code = parser.parse(input_string)
if python_code == "":
    print("ERRO NA TRADUÇÃO. PROGRAMA ABORTADO.")

else:
    output_file = open("func.py", "w")
    output_file.write(python_code)
    output_file.close()