#lista vazia serão adicionados os dicionários
personagens = []

for p in range(0,30):
    novo_p = {'cor':'verde','pontos':5, 'velocidade':'rapida'}
    personagens.append(novo_p)

#loop 2 fatiamento
for per in personagens[0:3]:
    if per['cor']== 'verde':
        per['cor']='amarelo'
        per['velocidade']='lenta'
        per['pontos']=10

#loop 3 fatiamento
for per2 in personagens[0:5]:
    print(per2)
print('...')    

