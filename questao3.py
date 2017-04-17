"""
envolve uma função que chama a si mesma. Embora possa não parecer muito, a recursão nos permite escrever soluções elegantes para problemas que, de outra forma, podem ser muito difíceis de programar.
"""
Num1 = int(input("Digite o primeiro número inteiro para ser exibido: "))
Num2 = int(input("Digite o segundo número inteiro para ser exibido: "))

def Imprima(Num1, Num2):
   print(Num1)
   if (Num1 == Num2):
       return Num2
   return Imprima(Num1 + 1, Num2)
   
Imprima(Num1, Num2)
