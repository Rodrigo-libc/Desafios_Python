def nomes(primeiro,segundo,meio=''): # essa função tem a seguintes condições
    if meio:                         #if else para caso alguém queira adicionar um 3 nome
        nome_completo = primeiro+' '+meio+' '+segundo #senão ele executara o bloco else
    else:
        nome_completo = primeiro+' '+segundo#que no caso sera apenas 1, e 2 nome
    return nome_completo.title()

result = nomes('rodrigo',meio='albuquerque',segundo='freitas')
print(result)
result = nomes('rodrigo','freitas')
print(result)  
