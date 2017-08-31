file = 'texto.txt'#variável que armazena o arquivo
#imprime as linhas do arquivo de texto em um loop for
with open(file) as file_object:
    linhas = file_object.readlines()
    
pi_string = ''
#loop fora do bloco
for linha in linhas:
    pi_string += linha.rstrip()
print(pi_string)
print(len(pi_string))