from hds_lexer import HDS_Lexer
from hds_parser import HDS_Parser

parser = HDS_Parser()

input_file = open("input.show", "r")
read = input_file.read()
input_file.close()

res = parser.parse(read)

def conserta_newlines (s):
    print(s)
    final = ''
    indent_atual = 0
    for c in s:
        if c == '{':
            indent_atual += 1
        elif c == '}':
            indent_atual -= 1
        elif c == '\n':
            final = final + '\n' + indent_atual * '\t'
        else:
            final = final + c

    return final

res = conserta_newlines(res)
print(res)

output_file = open("horadoshow.py", "w")
output_file.write(res)
output_file.close()