N = int(input('Digite um número: '))
Total = 0
for C in range(1, N + 1):
    if N % C == 0:
        Total += 1
    else:
        print(end='') 
print(N)
if Total == 2:
    print('Este número é primo!')
else:
    print('Este número não é primo!')        