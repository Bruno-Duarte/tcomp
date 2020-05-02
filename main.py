from mt import MaquinaDeTuring
from utils import cadeia_valida, descricao_mt, carrega_mt
from menus import *
	
				
def main():
	while True:
		linha()
		opc = menu_principal()
		linha()
		nova_cadeia = False
		if opc == 1:
			while True:
				if not nova_cadeia:
					try:
						arquivo = input('Nome do arquivo: ')
						tupla = tuple(carrega_mt(arquivo))
					except FileNotFoundError:
						linha()
						print('Arquivo não encontrado!')
						break
				
				while True:
					w = input('Cadeia de entrada [exem.: 0011]: ')
					if cadeia_valida(tupla[1], w):
						break
			
				linha()
				mt = MaquinaDeTuring(tupla, w)
				aceita = mt.processa_cadeia()
				if aceita:
					print(f'A máquina aceita {w}')
				else:
					print(f'A máquina rejeita {w}')
				linha()
				
				nova_cadeia = menu_secundario()
				if not nova_cadeia:
					break
				linha()	
		elif opc == 2:
			while True:
				if not nova_cadeia:
					tupla = tuple(descricao_mt())
				
				while True:
					w = input('Cadeia de entrada [exem.: 0011]: ')
					if cadeia_valida(tupla[1], w):
						break
			
				linha()
				mt = MaquinaDeTuring(tupla, w)
				aceita = mt.processa_cadeia()
				if aceita:
					print(f'A máquina aceita {w}')
				else:
					print(f'A máquina rejeita {w}')
				linha()
				nova_cadeia = menu_secundario()
				if not nova_cadeia:
					break
				linha()
		elif opc == 3:
			break
		else:
			print('Opção inválida!')
		
	
if __name__ == '__main__':
	main()
