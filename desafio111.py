linguagens = {
'rodrigo':['python','ruby'],
'ana':['go','haskell'],
'kum':['c','perl'],
}

for nome, linguagem in linguagens.items():
    print('\n'+nome.title()+' sua linguagem favorita e :')
    for l in linguagem:
        print('\t'+l.title())
        

