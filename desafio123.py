"""
Definimos loop while True, a variável cidade recebe a mensagem de m1 pedindo para
usuario digitar os lugares que ela visitou, se o que ele digitar for igual a sair break , ele para
e e o loop acaba, senão sera executado o bloco else, que faz uma concatenção
com a frase que o usuario digitou...
"""
m1 = 'Digite os lugares que vc visitou '
m1 += 'digite "sair" acabar. '
while True:
    cidade = input(m1)
    if cidade  == 'sair':
        break
    else:
        print('Eu adoraria ir para '+cidade+' !')

