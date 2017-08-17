m1 = 'Digite algo para ficar em processo ..'
m1 += 'Digite "sair" !'

mensagem = ""
while mensagem != 'sair':
    mensagem =input(m1)
    if mensagem != 'sair':
        print(mensagem)
