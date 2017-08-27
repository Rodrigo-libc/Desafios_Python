                                #classes
                    #Programação orientada a objetos no Python                 
class cachorro():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def sentar(self):
        print(self.nome.title()+' esta agora sentado')
    
    def por_toda_parte(self):
        print(self.nome.title()+' esta por toda parte !')
    
    def rolar(self):
        print(self.nome.title()+' esta rolando kkk !')
    
meu_dog = cachorro('Tor',6)
meu_dog2 = cachorro('Billy',3)

print('Meu cachorro mais novo se chama: '+meu_dog2.nome.title())
print('E ele tem: '+str(meu_dog2.idade)+' de idade')
meu_dog2.sentar()

print('\nO outro se chama: '+meu_dog.nome.title())
print('Ele tem '+str(meu_dog.idade)+' anos de idade')
meu_dog.rolar()        
    