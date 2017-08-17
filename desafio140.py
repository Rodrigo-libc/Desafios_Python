def nome_form(primeiro,segundo):  
    nome_completo = primeiro+' '+segundo #Função recebe primeiro e segundo nome
    return nome_completo.title() # retornado nome completo

while True:
    #loop while pra interação com o usuário
    print('Por favor diga seu nome: ')
    print('digite "q" para sair: ')
    #para sair do programa
    p_name = input('primeiro: ')
    if p_name == 'q':
        break
    u_name = input('ultimo: ')
    if u_name == 'q':
        break
    nome_formatado = nome_form(p_name, u_name)
    print('ola '+nome_formatado)
    
    
    

