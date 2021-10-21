def multiplo(x,y):
    if x != 0 and y%x == 0:
        print('São múltiplos')
    else:
        print('Não são múltiplos')
x = int(input("Número 1: "))
y = int(input("Número 2: "))
multiplo(x, y)