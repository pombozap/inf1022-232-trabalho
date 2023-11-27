import sys

### funcao traduzida do .show ###
def programa(X):
	X = 0
	RESULT = NUM
	while X > NUM:
		NUM = 1 + NUM
		for EXECUTE in range(5):
			RESULT = RESULT + NUM
			
		RESULT = RESULT * NUM
		if X >= NUM:
			X = NUM
			
		else:
			if X > NUM:
				X = 500
				
			else:
				if X > 500:
					X = 500
					
				
			
		Z = RESULT
		
	while X > NUM:
		while X > NUM:
			while X > NUM:
				while X > NUM:
					while X > NUM:
						X = X
						
					
				
			
		
	
	return (Z,)

### leitura dos argumentos do terminal ###
args = ()
for i in sys.argv[1:]:
	args += (int(i),)

(X,) = args

### rodando o programa ###
output = programa(X)

### imprimindo os valores das saidas rotulados no terminal ###
varnames = 'Z'.replace(' ','').replace('\n','').replace('\t','').split(',')
for i in range(len(varnames)):
	print(varnames[i], '=', output[i])

