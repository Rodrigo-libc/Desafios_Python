def fazer_pizza(*coberturas):
    """--mostrar a lista de coberturas--"""
    
    print(' preparando a pizza com as seguintes coberturas:\n')
    for p in coberturas:
           print('-'+p)
    """função usando * , nesse caso vai mostrar as coberturas
        mesmo se na chamada da função, tivesse apenas 1 valor"""

fazer_pizza('tomate','queijo','calabresa','pimenta')

