# importa apenas a clase CachorroSimples do arquivo Cachorro.py
# from CachorroSimp import CachorroSimples

#importa todas as classes para Cachorro
from Cachorro import *


print("Cachorro Simples:\n")

Bob = CachorroSimples("Bob")

print("nome: " + Bob.nome)
print("porte: " + Bob.porte)

print("alterando atributos do cachorro\n");

Bob.nome = "Bobie"
Bob.porte = "grande"

print("nome: " + Bob.nome)
print("porte: " + Bob.porte)

Bob.latir()



print("\n\nCachorro Seguro:\n")




Rex = CachorroSeguro("Rex")

#Os atributos dos objetos estão protegidos, portanto este meio de visualização e alteração não irão funcionar, portanto, serão ignorados
#Rex.nome = "Rexie"
#Rex.__nome = "Rexie"
#print("nome: " + Rex.__nome)
#print("porte: " + Rex.nome)


print("nome: " + Rex.pegarNome())
print("porte: " + Rex.pegarPorte())

print("alterando atributos do cachorro\n");

Rex.gravarNome("Rexie")
Rex.gravarPorte("pequeno")

print("nome: " + Rex.pegarNome())
print("porte: " + Rex.pegarPorte())

print("\nRex Latindo:")
Rex.latir()

#a calsse achorro seguro possui um metodo estatico, isso é, não precisa ser declarado para chamar
print("\nCachorro generico latindo")
CachorroSeguro.latir()