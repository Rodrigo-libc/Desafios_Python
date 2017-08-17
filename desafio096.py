personagem = {'posição_x':0 ,'posição_y': 25, 'velocidade': 'medio'}

print('posição original: '+str(personagem['posição_x']))
# Mova o alienígena para a direita
if personagem['velocidade'] == 'lenta':
    incremente_x= 1
elif personagem['velocidade'] == 'medio':
    incremente_x= 2
else:
    incremente_x= 3
# A posição antiga mais o incremento.
personagem['posição_x']  = incremente_x

print('nova posição: '+str(personagem['posição_x']))
