file = 'texto.txt'#variável que armazena o arquivo
#imprime as linhas do arquivo de texto em um loop for
with open(file) as file_object:
    for linha in file_object:
        print(linha.rstrip()) #remove as linhas em branco 
        