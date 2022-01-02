from Matematica import *

n1 = 20
n2 = 11
print(str(n1) + " e " + str(n2))
#chamando metodos 'estasticos' (sem a declaração de um objeto)
print("soma = " + str(Contas.soma(n1,n2)))
print("subtracao = "+str(Contas.subtracao(n1,n2)))
print("multiplicacao = "+str(Contas.multiplicacao(n1,n2)))
print("divisao = "+str(Contas.divisao(n1,n2)))
print("resto = "+str(Contas.modular(n1,n2)))

