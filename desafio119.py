#O script pega o valor do numero digitado e divide por 2 se o resto for igual a 0
#o resultado e par senão e impar
numero= input('Digite um numero para saber se e par ou impar ... ')
numero=int(numero)
if numero % 2 == 0:
    print('\nO número '+str(numero)+' e par')
else:
    print('\nO numero '+str(numero)+' e impar')

