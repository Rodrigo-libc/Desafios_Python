linguagens_favoritas={
'rodrigo':'python',
'greicy':'cobol',
'sergio':'c#',
}

amigos = ['rodrigo','sergio','greicy']

for nome in linguagens_favoritas.keys():
    print(nome.title())
    

    if nome in amigos:
        print('Oi '+nome.title()+
                ', essa e sua linguagem favorita '+linguagens_favoritas[nome].title()+'!')
    
