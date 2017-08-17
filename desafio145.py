def construir(primeiro,ultimo, **info_user):
    """Crie um dicionário contendo tudo o que sabemos sobre um usuário."""
    perfil = {}
    perfil['primeiro_nome']= primeiro
    perfil['ultimo']= ultimo
    for chave,valor in info_user.items():
        perfil[chave] = valor
    return perfil
user_perfil = construir('rodrigo','freitas',
                        local = 'recife', trabalho = 'redes')
print(user_perfil)
