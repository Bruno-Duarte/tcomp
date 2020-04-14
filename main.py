import re

def descricao_mt():
	print('Descrição da MT')
	print('Obs: Não use parênteses ou chaves nas entradas')
	Q = input('Estados [exem.: q1, q2, ..., qn]: ')
	sigma = input('Alfabeto de entrada [exem.: 0, 1, ..., n]: ')
	gamma = input('Alfabeto da fita [exem.: a, b]: ')
	funcao_transicao = descricao_transicoes(Q, gamma)
	return Q, sigma, gamma, funcao_transicao
	
def string_em_lista(string):
	lista = re.split(', | |,', string)
	return lista
	
def descricao_transicoes(Q, gamma):
	Q = string_em_lista(Q)
	gamma = string_em_lista(gamma)
	tabela = []
	linha = []
	for q in Q:
		for simbolo in gamma:
			transicao = input(f'Transição estado {q}, simbolo {simbolo} [exem.: (q1, x, D)]: ')
			transicao = string_em_lista(transicao)
			linha.append(transicao)
		tabela.append(linha)
	return tabela
				
	
def cadeia_valida(sigma, cadeia_entrada):
	for c in cadeia_entrada:
		if c not in sigma:
			print('A cadeia possui símbolos que não estão no alfabeto')
			return False
		else:
			return True	

def processa_cadeia():
	w = input('Cadeia de entrada [exem.: 001011]: ')
	

def main():
	mt = descricao_mt()
	for linha in mt[3]:
		for coluna in linha:
			print(coluna, end=' ')
	print()
	
if __name__ == '__main__':
	main()
