class carro():
    #classe para um carro
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def nome_descritivo(self):
        nome_longo = str(self.ano)+' '+self.marca+' '+self.modelo
        return nome_longo.upper()
     
    def ler_km(self):
     #Imprima uma declaração mostrando a quilometragem do carro.
        print('\nEsse carro rodou: '+str(self.odometro)+' km')
        
     #Defina a leitura do odômetro         
    def atualizar_odometro(self,quilometros):
        #Rejeite a alteração
        if quilometros >= self.odometro:
            self.odometro = quilometros
        else:
            print('você não pode reverter o odômetro ')
            #incremetro
    def incremento_odo(self,miles):
        self.odometro += miles
                  
#meu_novo_carro = carro('audi','a4',2017)

#meu_novo_carro.atualizar_odometro(21)
#A mensagem sera exibida, pois 21 não e maior nem igual ao valor do odômetro
#O valor do odõmetro e 23
#meu_novo_carro.ler_km()

#print(meu_novo_carro.nome_descritivo())

meu_user_car = carro('HR-V','honda',2017)

meu_user_car.atualizar_odometro(23500)

print(meu_user_car.nome_descritivo())

meu_user_car.ler_km()

meu_user_car.incremento_odo(100) #receberá + 100 na quilometragem

meu_user_car.ler_km()





