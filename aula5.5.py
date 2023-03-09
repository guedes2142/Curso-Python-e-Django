# Dicionarios 
# Dicionarios são hashmaps armazenam pares de keys e values, para declarar um dicionario usamos {}.
d = {'Nome': 'Rafael guedes', 'Cidade': 'Suzano', 'Estado': 'São paulo', 'Idade': '34'}
print(d) # {'Nome': 'Rafael guedes', 'Cidade': 'Suzano', 'Estado': 'São paulo', 'Idade': '34'}
# observe pode retornado em outra ordem  por isso são hashmaps o local onde fica guardado
# cada resultada depende de uma valor computado de um hash calucalado a partir desse objeto.
#para acessar uma key(chave) no dicionari usamos []
diconario = d['Nome']
print(diconario)# Rafael guedes
#para atualizar
diconario = d['Nome'] = 'Rafael Almeida'
print(d)# {'Nome': 'Rafael Almeida', 'Cidade': 'Suzano', 'Estado': 'São paulo', 'Idade': '34'}
#para verificar se uma key está no dicionario podemos usar o in
esta = 'asdf' in d
print(esta)# False
# para verificar o valor usamos d.values()
esta = 'Suzano' in d.values()
print(esta)# True
# para acessar chave sem erros usamos o metodo get()
esta = d.get('asdf')
print(esta) # None 
esta = d.get('asdf', 'não está')
print(esta) # não está
# para saber quantos elementos tem dentro do dicionario usamos a função len()
esta = len(d)
print(esta) # 4
esta = d.keys() #informa quais são as keys
print(esta)  # ['Nome', 'Cidade', 'Estado', 'Idade'])
esta = d.values()#informa quais são os values
print(esta) # (['Rafael Almeida', 'Suzano', 'São paulo', '34'])
esta = d.items()# retotna tudo dentro de tuplas
print(esta) # ([('Nome', 'Rafael Almeida'), ('Cidade', 'Suzano'), ('Estado', 'São paulo'), ('Idade', '34')])
d['olá'] = 'mundo!'
print(d) # {'Nome': 'Rafael Almeida', 'Cidade': 'Suzano', 'Estado': 'São paulo', 'Idade': '34', 'olá': 'mundo!'}
k = tuple(d.keys())
print(k) #('Nome', 'Cidade', 'Estado', 'Idade', 'olá')
v = tuple(d.values())
print(v)#('Rafael Almeida', 'Suzano', 'São paulo', '34', 'mundo!')
i = tuple(d.items())
print(i)#(('Nome', 'Rafael Almeida'), ('Cidade', 'Suzano'), ('Estado', 'São paulo'), ('Idade', '34'), ('olá', 'mundo!'))
# os dicionarios são hashmaps por que as cheves precisçao ser objetos imútaveis
l = [1,2,3]
# d[l] = 'Pode?' #TypeError: unhashable type: 'list'
#já os valores podem ser mutaveis
d.update(interesses = ['bebida', 'vodka'])
print(d) # {'Nome': 'Rafael Almeida', 'Cidade': 'Suzano', 'Estado': 'São paulo', 'Idade': '34', 'olá': 'mundo!', 'interesses': ['bebida', 'vodka']}
d['interesses'].append('algo')
print(d) #{'Nome': 'Rafael Almeida', 'Cidade': 'Suzano', 'Estado': 'São paulo', 'Idade': '34', 'olá': 'mundo!', 'interesses': ['bebida', 'vodka', 'algo']}
d.pop('interesses')
print(d)# {'Nome': 'Rafael Almeida', 'Cidade': 'Suzano', 'Estado': 'São paulo', 'Idade': '34', 'olá': 'mundo!'}
t = tuple(d.items())
dict(t)
print(t)