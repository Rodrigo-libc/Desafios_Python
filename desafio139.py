def pessoa(primeiro,segundo,idade=''):
    rodrigo = {'pri':primeiro,'seg':segundo}
    if idade:
        rodrigo['idade']=idade # Se existir idade na função com valor vazio.
            return rodrigo     # Então ele adiciona a chave, e o argumento ao dicionário
       #retorna o dicionário
nome = pessoa('rodrigo','freitas',22) # nome recebe a função
print(nome)
