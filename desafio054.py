minhas_frutas= ['abacaxi','maça','melancia','abacate']
frutas_amigos = minhas_frutas[:]
minhas_frutas.append('banana')
frutas_amigos.append('laranja')

print('Frutas que Amo\n')

for fruta in minhas_frutas:
    print('eu amo '+fruta.capitalize())

print('\nFrutas que meus amigos amam\n')
for fruta2 in frutas_amigos:
        print('meus amigos amam '+fruta2.capitalize())

