pizza ={
'pizza':'fatiada',
'coberturas':['cogumelos','queijo extra'],
}

#resumindo o pedido
print('você pediu uma Pizza '+pizza['pizza']+' com as seguintes coberturas')
for c in pizza['coberturas']:
    print('\t => '+c)
    


