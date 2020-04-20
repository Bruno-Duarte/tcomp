from menus import titulo

class MaquinaDeTuring():

	def __init__(self, tupla, w):
		self.tupla = tupla
		self.w = list(w + '__')
	
	def processa_cadeia(self):
		q = self.tupla[4]
		fita = [q] + self.w
		delta = self.tupla[3]
		cabecote = 1
		
		titulo()
		_fita = ' '.join(fita)
		print(_fita)
		while True:
			if 'D' in delta[q][fita[cabecote]] or 'd' in delta[q][fita[cabecote]]:
				fita[cabecote-1] = delta[q][fita[cabecote]][1]
				fita[cabecote] = delta[q][fita[cabecote]][0]
				q = fita[cabecote]						
				cabecote += 1
			elif 'E' in delta[q][fita[cabecote]] or 'e' in delta[q][fita[cabecote]]:
				estado = delta[q][fita[cabecote]][0]
				fita[cabecote] = delta[q][fita[cabecote]][1]
				fita[cabecote-1] = fita[cabecote-2]
				fita[cabecote-2] = estado
				q = fita[cabecote-2]
				cabecote -= 1	
			_fita = ' '.join(fita)
			print(_fita)	
			
			if q == self.tupla[5] or q == self.tupla[6]:
				return q == self.tupla[5]

