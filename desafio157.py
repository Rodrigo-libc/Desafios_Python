from carro2 import carro_eletrico

meu_carro = carro_eletrico('audi','a4',2017)
print(meu_carro.nome_descritivo())
meu_carro.battery.describe_battery()
meu_carro.battery.get_range()



