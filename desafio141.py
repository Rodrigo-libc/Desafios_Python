def nome_users(nomes): #função com parâmetro nomes
    for nome in nomes: #para cada nome na função nomes, 'nome' recebe uma msg.
        msg = 'Hola '+nome.title() #msg que será exibida a cada pessoa.
        print(msg) #msg e mostrada na tela
lista_users = ['rodrigo','ana','lucas']# lista com os nomes dos usuários
nome_users(lista_users) # foi passado a lista com os nomes na função.


