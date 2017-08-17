# criamos uma variável com valor True para o loop while
# colocamos um input() para que o usuário digite algo
# se o que o usuário digitar for == a "sair" a variável se torna false 
# e o loop acaba, se for qualquer outra coisa então então sera executado o bloco
#else e sera exibida a oque ele digitou ..
m1 = '!loop em processo: '
ativo = True
while ativo:
    mensagem = input(m1)
    if mensagem == 'sair':
        ativo = False
    else:
        print(mensagem)

