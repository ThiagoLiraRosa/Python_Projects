import random
num = random.randint (1, 5)
game=int(input('Adivinhe o Número que o Computador pensou !'))
if game == num:
    print('Você Acertou! O número foi {} !'.format(num))
else:
    print('Você Errou! O computador pensou no número {} !'.format(num))


