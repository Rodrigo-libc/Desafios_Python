file = 'rodrigo.txt'
try:
    with open(file) as f_obj:
        conteudo = f_obj.read()
    #O arquivo não existe nesse caso sera mostrado a mensagem.
except FileNotFoundError:
    print('Desculpe o arquivo '+file+' não existe .')
    
    
    
    