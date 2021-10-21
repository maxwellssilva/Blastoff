N1 = int(input('Digite um número: '))
N2 = int(input('Digite um número: '))
N3 = int(input('Digite um número: '))
MENOR = N1
if N3 < N1 and N3 < N2:
    MENOR = N3
if N2 < N1 and N2 < N3:
    MENOR = N2  
print('O menor valor é {}'.format(MENOR))     