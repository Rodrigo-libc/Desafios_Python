coberturas_disponiveis = ['tomate','queijo','pimenta verde','azeitona']

coberturas_pedidos =['tomate','batata frita','azeitona']

for cobertura in coberturas_pedidos:
    if cobertura in coberturas_disponiveis:
        print('\nadicionando '+cobertura)
    else:
        print('\ndesculpe não temos mais '+cobertura)
print('\npizza pronta')

