class Valor:
	def __init__(self, num_a, num_b):
		self.num_a = num_a
		self.num_b = num_b
	
	def soma(self):
		return self.num_a + self.num_b
	
	def subtracao(self):
		return self.num_a - self.num_b
	
	@property
	def num_a(self):
		return self._num_a
	
	@num_a.setter
	def num_a(self, valor):
		if not isinstance(valor, (int, float)):
			print('O valor A deve ser do tipo numerico')
			valor = float(input("Informe o valor dnv: "))
		self._num_a = valor
		
	@property
	def num_b(self):
		return self._num_b
	
	@num_b.setter
	def num_b(self, valor):
		if not isinstance(valor, (int, float)):
			
			print('O valor B deve ser do tipo numerico')
			valor = float(input("Informe dnv o valor: "))
		self._num_b = valor


