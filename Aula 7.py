#+ Adição
#- Subtração
#* Multiplicação
#/ Divisão
#** Potência (Elevado ao Quadrado exemplo: 5x5)
#// Divisão inteira
#% Resto da Divisão
#Ordem de Precedência#
#1º () execulta primeiro
#2º **
#3º *, /, //, %
#4º + e -
n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
a=n1+n2
b=n1*n2
c=n1-n2
d=n1/n2
e=n1//n2
f=n1**n2
g=n1%n2
print("A soma é {}, o produto é {}, s subtração é {}, a divisão é {:.2f} ".format(a, b, c, d))
print("A divisão inteira, {} e a potência é {} e o resto de divisão é {}".format(e, f, g))
