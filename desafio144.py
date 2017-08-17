def fazer_pizza(tamanho,*coberturas):
    """resumo da pizza que será feita"""
    print('o tamanho da pizza e: '+str(tamanho)+' com as seguintes coberturas')
    for cobertura in coberturas:
        print('-'+cobertura)
fazer_pizza(16,'tomate','queijo','calabresa')