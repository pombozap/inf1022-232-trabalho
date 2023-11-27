import sys

### funcao traduzida do .show ###
def programa(X, Y):
	Z = 0
	B = Y
	C = X
	for EXECUTE in range(5):
		Z = Z + 1
		if Z > 2:
			B = B + 1
			
		else:
			C = C * 2
			
		
	A = 0
	while A <= 10:
		A = A + 1
		
	
	return (A, B, C,)

### leitura dos argumentos do terminal ###
args = ()
for i in sys.argv[1:]:
	args += (int(i),)

(X, Y,) = args

### rodando o programa ###
output = programa(X, Y)

### imprimindo os valores das saidas rotulados no terminal ###
varnames = 'A, B, C'.replace(' ','').replace('\n','').replace('\t','').split(',')
for i in range(len(varnames)):
	print(varnames[i], '=', output[i])

