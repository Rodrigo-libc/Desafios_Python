print('Digite 2 numeoros para adivisão .')
print('digite "q" enter para sair')

while True:
    primeiro = input('Primeiro número :')
    if primeiro == 'q':
        break
    segundo = input('Segundo número :')
    #bloco Try
    try:
        total = int(primeiro) / int(segundo)
    except ZeroDivisionError:
        print('você não pode dividir o 0')
    else:
        print(total)
    