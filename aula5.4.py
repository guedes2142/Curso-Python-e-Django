#Tuplas
#para declarar uma tupla devemos usar o seguinte codigo:
('a', 'b', 'c')
t = ('a', 'b', 'c')
# tuplas são sequiencias imutaveis, qualquer operação nela ira retornar um novo objeto com 
# o resultado
# Os métodos da tuplas são poucos:
# t.
# t.count t.index
print(type(t))# <class 'tuple'>
# toda sequiancia e um interavel inclusivel as strings
r = tuple('Rafael')
print(r) # ('R', 'a', 'f', 'a', 'e', 'l')
# o consulto da tupla percorre item a item armazenando nos indexes da tupla
# Podemos também passar lista dentro da tupl
t = tuple([1,2,3,4,5])
print(t)# (1, 2, 3, 4, 5)
# Assim como na lista o tupla suporta qualquer tipo de objeto
t = ('a', 1, 1.14, (2j, len),[1,2,3])
print(t)# ('a', 1, 1.14, (2j, <built-in function len>), [1, 2, 3])
#sendo uma sequência podemos usar indexes
print(t[0], t[1]) # a 1
# o que define a tupla é a virgula , e não exatamente os ()
t = 'a', # com virgula retorna uma tupla
s = 'a' # sem virgula retorna uma string
print(f'{t}\n'# ('a',)
      f'{s}') #   a
# exemple do por que usar ()
t = 'c', 'd', 'e',
# print('a','b','c' + t) # TypeError: can only concatenate str (not "tuple") to str
# então colocamos ()
print(('a','b','c') + t) #('a', 'b', 'c', 'c', 'd', 'e')
# para criar uma tupla fazia usamos
tuple()
()
print(type(()))
