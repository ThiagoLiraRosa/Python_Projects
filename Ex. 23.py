'''num=input('Digite um número de 0 a 9999: ')
num2=num.split()
print('Unidade: {}'.format(num2[0][3]))
print('Dezena: {}'.format(num2[0][2]))
print('Centena: {}'.format(num2[0][1]))
print('Milhar: {}'.format(num2[0][0]))'''

num=int(input('Digite um número de 0 a 9999: '))
u=num // 1 % 10
d=num //10 % 10
c=num // 100 % 10
m=num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))