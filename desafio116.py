>>> idade = input('Digite sua idade ...')
Digite sua idade ...22
>>> idade >= 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 

#Nesse exemplo o erro acontece por que a entrada de dados no python 
#são consideradas como strings, então para resolver vc precisa converter
#o numero para um valor int() inteiro

>>> idade = int(idade)
>>> idade >= 18
True
>>> 

