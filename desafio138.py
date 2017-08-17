def pessoa(primeiro,segundo):
    #retorne dicionário
    rodrigo = {'pri':primeiro,'seg':segundo}
    return rodrigo
nome = pessoa('rodrigo','freitas')
print(nome)

for i,n in nome.items(): # loop de teste e.e x:D
    print('\n'+i+':',n)