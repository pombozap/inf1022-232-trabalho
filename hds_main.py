import os.path as path
from hds_parser import HDS_Parser

def read_file_name (extension):
    file_name = ""
    while not file_name:
        file_name = input("  > ")

    if file_name == "EXIT":
        exit()

    if file_name[-len(extension):] != extension:
        file_name += extension

    return file_name

def get_file_name (extension, tipo):
    print("\n    Digite o nome do arquivo %s de %s ou EXIT para sair:"%(extension, tipo))

    return read_file_name(extension)

def check_file_exists (file_name):
    if path.isfile(file_name):
        largura_caixa = max(29, len(file_name))
        mensagem_sucesso = "\n    +-%s-+\n    | %s |\n    | %s |\n    | %s |\n    +-%s-+\n"%(
            '-' * largura_caixa,
            'ARQUIVO .show ENCONTRADO:'.center(largura_caixa, ' '),
            ' ' * largura_caixa,
            file_name.center(largura_caixa, ' '),
            '-' * largura_caixa,
        )
        print(mensagem_sucesso)
        return True
    
    else:
        largura_caixa = 22 + len(file_name)
        mensagem_erro = "\n    +-%s-+\n    | %s |\n    | %s |\n    | %s |\n    +-%s-+\n"%(
            '-' * largura_caixa,
            'ERRO:'.center(largura_caixa, ' '),
            ' ' * largura_caixa,
            'ARQUIVO %s NÃO EXISTE.'%file_name,
            '-' * largura_caixa,
        )
        print(mensagem_erro)
        return False

def get_input_file ():
    input_file_name = get_file_name(".show", "entrada")
    
    while not check_file_exists(input_file_name):
        input_file_name = read_file_name(".show")

    return input_file_name

### programa ###
parser = HDS_Parser()
input_file_name = get_input_file()

input_file = open(input_file_name, "r")
input_string = input_file.read()
input_file.close()

python_code = parser.parse(input_string)

if python_code == None:
    exit(1)

else:
    mensagem_sucesso = """
    +-------------------------------+
    | TRADUÇÃO TERMINADA COM ÊXITO. |
    |                               |
    |  ESCOLHA O ARQUIVO DE SAÍDA.  |
    +-------------------------------+
    """
    print(mensagem_sucesso)

output_file_name = get_file_name(".py", "saída")

output_file = open(output_file_name, "w")
output_file.write(python_code)
output_file.close()

largura_caixa = max(29, len(output_file_name))
mensagem_final = "\n    +-%s-+\n    | %s |\n    | %s |\n    | %s |\n    +-%s-+\n"%(
        '-' * largura_caixa,
        "PROGRAMA GRAVADO EM:".center(largura_caixa, ' '),
        ' ' * largura_caixa,
        output_file_name.center(largura_caixa, ' '),
        '-' * largura_caixa
    )
print(mensagem_final)
