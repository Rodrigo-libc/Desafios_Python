file = 'texto.txt'#variável que armazena o arquivo
#imprime as linhas do arquivo de texto em um loop for
with open(file) as file_object:
    linhas = file_object.readlines()
#loop fora do bloco
for linha in linhas:
    print(linha.rstrip()) #remove as linhas em branco