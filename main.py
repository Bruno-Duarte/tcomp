import re

def descricao_mt():
	print('Descrição da MT')
	print('Obs: Não use parênteses ou chaves nas entradas')
	Q = input('Estados [exem.: q0, q1, q2, ..., qn]: ')
	sigma = input('Alfabeto de entrada [exem.: 0, 1, ..., n]: ')
	gamma = input('Alfabeto da fita [exem.: a, b]: ')
	delta = descricao_transicoes(Q, gamma)
	return Q, sigma, gamma, delta
	
def string_em_lista(string):
	lista = re.split(', | |,', string)
	return lista
	
def descricao_transicoes(Q, gamma):
	Q = string_em_lista(Q)
	gamma = string_em_lista(gamma)
	delta = {}
	transicoes_estado = {}
	for q in Q:
		for simbolo in gamma:
			transicao = input(f'Transição estado {q}, simbolo {simbolo} [exem.: (q1, x, D)]: ')
			transicao = string_em_lista(transicao)
			tupla = tuple(transicao)
			transicoes_estado[simbolo] = tupla
		delta[q] = transicoes_estado
		transicoes_estado = {}
	return delta
				
	
def cadeia_valida(sigma, cadeia_entrada):
	for c in cadeia_entrada:
		if c not in sigma:
			print('A cadeia possui símbolos que não estão no alfabeto')
			return False
		else:
			return True	

def processa_cadeia(w, delta, q0):
	q = q0
	w = w + '__'
	cabecote = 1
	configuracao = list(w)
	configuracao = [q] + configuracao
	while True:
		if 'd' in delta[q][configuracao[cabecote]]:
			configuracao[cabecote-1] = delta[q][configuracao[cabecote]][1]
			configuracao[cabecote] = delta[q][configuracao[cabecote]][0]
			q = configuracao[cabecote]						
			cabecote += 1
		elif 'e' in delta[q][configuracao[cabecote]]:
			estado = delta[q][configuracao[cabecote]][0]
			configuracao[cabecote] = delta[q][configuracao[cabecote]][1]
			configuracao[cabecote-1] = configuracao[cabecote-2]
			configuracao[cabecote-2] = estado
			q = configuracao[cabecote-2]
			cabecote -= 1	
		print(configuracao)	
		if q == 'qa' or q == 'qr':
			break
		
				
def main():
	mt = descricao_mt()
	w = input('Cadeia de entrada [exem.: 001011]: ')
	processa_cadeia(w, mt[3], 'q0')
	
if __name__ == '__main__':
	main()
