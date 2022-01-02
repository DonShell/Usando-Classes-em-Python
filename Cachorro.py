class CachorroSimples:
	nome = ""
	porte = "medio"

	def __init__(self, nome):
		self.nome = nome
	
	def latir(self):
		print("AuAuAuAuAu!")

class CachorroSeguro:
	#dois anderlines (__) na antes do nome faz com que a variavel seja privada e só possa ser acessada se chamada dentro desta classe
	__nome = ""
	__porte = "medio"

	def __init__(self, nome):
		self.__nome = nome

	#esta é uma classe estatica e não precisa de self para trabalhar
	@staticmethod
	def latir():
		print("AuAuAuAuAu!")

	def gravarPorte(self, porte):
		self.__porte = porte

	def pegarPorte(self):
		return self.__porte

	def pegarNome(self):
		return self.__nome
	
	def gravarNome(self, nome):
		self.__nome = nome
