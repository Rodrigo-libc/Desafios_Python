#O set() faz com que a mesma linguagem não seja repetida.

linguagens_favoritas ={
'luiza':'php',
'jorge':'javascript',
'messias':'c#',
'ana':'php'
}
for linguagem in set(linguagens_favoritas.values()):
    print(linguagem.title())
