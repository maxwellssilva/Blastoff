N = int(input('Digite um número: '))
print('A tabuada {} é: '.format(N))
for c in range (1, 11):
    print('%d x %d = %d' %(N, c, N*c))