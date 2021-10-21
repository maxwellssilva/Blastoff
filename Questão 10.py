N = int(input('Digite um número: '))
F = 1
for C in range (1, N + 1):
    F = F * C
print('O fatorial de {} é {}'.format(N, F))    