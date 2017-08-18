#lista vazia para armazenar os dicionarios
personagens = []

#loop for para fazer 30 personagens
for numero_personagem in range(30):
    
    novo_personagem = {'cor':'preto','pontos': 5,'velocidade':'lento'}
    
    personagens.append(novo_personagem)

#loop mostra os 5 primeiros dicionarios
for per in personagens[:5]:
    print(per)
print('...')

#mensagem que mostra a quantidade de dicionarios nesse caso 30
print('total de personagens => '+str(len(personagens)))



