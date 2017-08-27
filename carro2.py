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
        
#Classe battery        
class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("\nO carro tem " + str(self.battery_size) + "-kWh de bateria.")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        mensagem = '\nEsse carro pode ir aproximadamente '+str(range)
        mensagem += ' milhas com uma carga total'
        print(mensagem)
        
        #Herança <==>
class carro_eletrico(carro):
#Representa os aspectos de um carro, específico para veículos elétricos.
    def __init__(self,marca,modelo,ano):
    #Inicializar atributos da classe pai.
        super().__init__(marca, modelo,ano)
        self.battery = Battery()
