'''nome=str(input('Digite seu nome Completo: '))
print(nome.upper())
print(nome.lower())
div = nome.split()
nome2 = ''.join(div)
print('seu nome tem {} caracteres'.format(len(nome2)))
print('seu primeiro nome tem {} caracteres'.format(len(div[0])))'''

#Ou
nome=str(input('Digite seu nome Completo: ')).strip()
print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} caracteres'.format(nome.find(' ')))
lista=nome.split()
print('Seu nome é {} e ele tem {} letras.'.format(lista[0], len(lista[0])))