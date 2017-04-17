numeros = [1, 2 , 3 , 4 ,5]
alunos = {"201610040062": "Aparecida", "201610040063": "Maelly" , "201610040027": "Clara"}
mensagemProva4 = None
print("Seja bem vindo(a) ao Programa da Prova 4! \n")
print("O que é uma lista: Uma lista é uma sequência ou coleção ordenada de valores. Os valores que formam uma lista são chamados elementos ou itens. Listas são similares a strings, que são uma sequência de caracteres, no entanto, diferentemente de strings, os itens de uma lista podem ser de tipos diferentes.")
print("O que é um dicionário: São estruturas de dados que implementam mapeamentos; E um mapeamento é uma coleção de associações entre pares de valores. \n")
print("Estou pronto para manipular listas e dicionários na prova!")

import random
sorteados = []
for i in range(20):
  numero = random.randint(1 , 100)
  sorteados.append(numero)
  print("O valor da linha", i, "é: ",numero)
  
mensagemProva4 = "Prova  sobre manipulação de listas e dicionários! \n"
NLetras = len(mensagemProva4)
print("A quantidade de letras é", NLetras)
print("")
mensagemProva4 += "Prova  de  número  4."
print(mensagemProva4)


