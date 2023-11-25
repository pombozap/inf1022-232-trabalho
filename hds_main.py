from hds_parser import HDS_Parser

parser = HDS_Parser()

input_file = open("func.show", "r")
input_string = input_file.read()
input_file.close()

python_code = parser.parse(input_string)

if python_code != None:
    output_file = open("func.py", "w")
    output_file.write(python_code)
    output_file.close()
    print("""
            +------------------------------------+
            |    TRADUÇÃO TERMINADA COM ÊXITO.   |
            |                                    |
            |       DISPONÍVEL EM "func.py"      |
            +------------------------------------+
            """)