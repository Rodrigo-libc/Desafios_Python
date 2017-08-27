class carro():
    #classe para um carro
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def nome_descritivo(self):
        nome_longo = str(self.ano)+' '+self.marca+' '+self.modelo
        return nome_longo.title()
     
    def ler_km(self):
     #Imprima uma declaração mostrando a quilometragem do carro.
        print('\nEsse carro rodou: '+str(self.odometro)+' km')
        
     #Defina a leitura do odômetro         
    def atualizar_odometro(self,quilometros):
        self.odometro = quilometros
                  
meu_novo_carro = carro('audi','a4',2017)

meu_novo_carro.atualizar_odometro(23)

meu_novo_carro.ler_km()

print(meu_novo_carro.nome_descritivo())

