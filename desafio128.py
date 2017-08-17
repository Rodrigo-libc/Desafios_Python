respostas ={}
#defina uma bandeira para indicar que cada pessoa esta ativa.
active = True
while active:
    #solicite o nome e a resposta da pessoa
    nome = input('Digite seu nome... ')
    resposta = input('Qual montanha você gostaria de escalar algum dia ? ')

    #guarde as respostas no dicionário
    respostas[nome]= resposta

    repetir = input('Gostaria de deixar outra pessoa responder? (sim/não) ')
    if repetir == 'não':
        active = False

#mostre os resultados.
print('\n---Resultados da Enquete---')
for n, r in respostas.items():
    print(n+' gostaria de escalar '+r)

