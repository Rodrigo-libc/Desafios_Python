def count(file):
    try:
        with open(file) as f_obj:
            conteudo = f_obj.read()
        
    except FileNotFoundError:
        msg = 'Desculpe o arquivo '+file+' não existe .'
        print(msg)
    
    else:
        word = conteudo.split()
        numero_word = len(word)
        print('O arquivo '+file+' tem '+str(numero_word)+' linhas .')
    
file = 'alice.txt'
count(file)