def mostrar_modelos(modelos,completos): # função para mostrar os modelos
    while modelos:
        modelo_atual = modelos.pop()
        print('mostrando modelo: '+modelo_atual)
        completos.append(modelo_atual)
        
def listar_modelos(completos): #função para listar
    print('\n--listando modelos--\n')
    for modelo_completo in completos:
        print(modelo_completo)

modelos= ['SSD','Processador','Monitor']
completos = []

mostrar_modelos(modelos,completos)
listar_modelos(completos)
        
    
    
        