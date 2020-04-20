import re
from menus import linha


def descricao_mt():
	print('Descrição da MT')
	print('Obs: Não use parênteses ou chaves nas entradas')
	while True:
		Q = input('Estados [exem.: q0, q1, ..., qn, qA, qR]: ')
		if len(Q) > 2:
			break
		else:
			linha()
			print('Q é inválido!')
	sigma = input('Alfabeto de entrada [exem.: 0, 1, ..., n]: ')
	while True:
		gamma = input('Alfabeto da fita [exem.: a, b, ..., _]: ')
		if alfabeto_valido(sigma, gamma):
			break
	delta = funcao_de_transicao(Q, gamma)
	while True:
		q0 = input('Especifique o estado inicial [exem.: q0]: ')
		qa = input('Especifique o estado de aceitação [exem.: qA]: ')
		qr = input('Especifique o estado de rejeição [exem.: qR]: ')
		if estado_valido(Q, q0, qa, qr):
			break
	return Q, sigma, gamma, delta, q0, qa, qr

	
def carrega_mt(arquivo):
	arquivo = open(arquivo, 'r')
	Q = sigma = gamma = q0 = qa = qr = _Q = _gamma = None 
	delta = {}
	transicoes_estado = {}
	ele = simbolo = q = 0
	for linha in arquivo:
		if linha[0] == '%':
			ele += 1
		elif ele == 1:
			Q = linha[:-1]
		elif ele == 2:
			sigma = linha[:-1]
		elif ele == 3:
			gamma = linha[:-1]
		elif ele == 4:
			if simbolo == 0:
				_Q = string_em_lista(Q)
				_gamma = string_em_lista(gamma)
			transicao = linha[:-1]
			if simbolo < len(_gamma):
				transicao = string_em_lista(transicao)
				tupla = tuple(transicao)
				transicoes_estado[_gamma[simbolo]] = tupla
				simbolo += 1
			if simbolo == len(_gamma):
				delta[_Q[q]] = transicoes_estado
				transicoes_estado = {}
				simbolo = 0
				q += 1
		elif ele == 5:
			q0 = linha[:-1]
		elif ele == 6:
			qa = linha[:-1]
		elif ele == 7:
			qr = linha[:-1]
		else:
			return None
	return Q, sigma, gamma, delta, q0, qa, qr
			
	
def string_em_lista(string):
	lista = re.split(', | |,', string)
	return lista

	
def funcao_de_transicao(Q, gamma):
	_Q = string_em_lista(Q)[:-2]
	gamma = string_em_lista(gamma)
	delta = {}
	transicoes_estado = {}
	
	for q in _Q:
		for simbolo in gamma:
			while True:
				transicao = input(f'Transição estado {q}, simbolo {simbolo} [exem.: q1, x, D]: ')
				transicao = string_em_lista(transicao)
				if transicao_valida(transicao[0], transicao[1], transicao[2], Q, gamma):
					break
			tupla = tuple(transicao)
			transicoes_estado[simbolo] = tupla
		delta[q] = transicoes_estado
		transicoes_estado = {}
	return delta
				
			
def estado_valido(Q, q0, qa, qr):
	Q = string_em_lista(Q)
	_Q = [q0] + [qa] + [qr] + []
	
	for q in _Q:
		if q not in Q:
			linha()
			print('Algum estado digitado não está contido em Q')
			return False
		else:
			return True
			
def alfabeto_valido(sigma, gamma):
	sigma = string_em_lista(sigma)
	gamma = string_em_lista(gamma)
	
	for c in sigma:
		if c not in gamma:
			linha()
			print('O alfabeto de entrada deve estar contido no alfabeto da fita')
			return False
		else:
			return True

		
def transicao_valida(q, simbolo, mov, Q, gamma):
	movs = ['D', 'd', 'E', 'e']
	
	if q not in Q or simbolo not in gamma or mov not in movs:
		linha()
		print('Transição inválida!')
		return False
	else:
		return True

def cadeia_valida(sigma, cadeia_entrada):
	for c in cadeia_entrada:
		if c not in sigma:
			linha()
			print('A cadeia possui símbolos que não estão no alfabeto')
			return False
		else:
			return True

