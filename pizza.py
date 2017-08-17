#importar no desafio 146
def fazer_pizza(tamanho,*coberturas):
    """Resuma a pizza que estamos prestes a fazer."""
    print('\nO tamanho da pizza e: '+str(tamanho)+' com as seguintes coberturas ')
    for p in coberturas:
        print('-'+p)
        

