palavra = str(input('Digite uma palavra: '))
unir = ''.join(palavra)
palin = unir[::-1]
if palin == unir:
    print('Esta palavra é um palíndromo')
else:
    print('Esta palavra não é um palíndromo')    