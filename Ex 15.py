dias=int(input('Por quantos dias o Carro foi alugado?: '))
km=float(input('Quantos km foram rodados?: '))
dias=dias*60
km=km*0.15
total=dias+km
print('O valor total a pagar é R$ {}. '.format(total))

#Outra maneira de fazer
#total2=(dias*60) + (km * 0.15)
#print(total2)