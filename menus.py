COMP_LINHA = 80

def menu_principal():
	print('1. Carregar entrada de um arquivo txt')
	print('2. Digitar entrada')
	print('3. Sair')
	try:
		opc = int(input('Digite sua opção: '))
	except ValueError:
		pass
	else:
		return opc 

	
def menu_secundario():
	nova_entrada = input('Processar nova cadeia? 1. Sim, 2. Não: ')
	return nova_entrada == '1'	


def linha():
	for i in range(COMP_LINHA):
		print('=', end='')
	print()

	
def titulo():
	print('--------------CONFIGURAÇÕES--------------')
