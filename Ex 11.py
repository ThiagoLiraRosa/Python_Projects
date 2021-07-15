alt=float(input('Digite a Altura da parede: '))
larg=float(input('Digite a Largura da parede: '))
area= alt * larg
tinta= area / 2
print('Uma parede de {:0.2f} metros, precisará de {:0.2f} litros de Tinta'.format(area, tinta))
