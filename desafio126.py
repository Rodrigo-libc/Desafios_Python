users_não_conf =['rodrigo','luiza','bruno','amanda']
users_conf = []
# Verifique cada usuário até que não haja mais usuários não confirmados.
# Mova cada usuário verificado, para a lista de usuários confirmados.
while users_não_conf:
    user_atual = users_não_conf.pop()

    print('verificando o usuário: '+user_atual.title())

    users_conf.append(user_atual)

# Exibe todos os usuários confirmados.
print('\nOs usuários a seguir foram confirmados: ')
for user_conf in sorted(users_conf):
     print(user_conf.title())

