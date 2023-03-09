
nome = 'Rafael' #variavel nome = recebe a string literal 'Rafael'
nomelen = len(nome)
print(nomelen) # 6 caraters
#string tbm são sequincia, sequincia  de letras
#se quiser saber qual o o elemento de uma string faermos um assesso por indexes nome[0] = R

print(nome[0])
#print(nome[6])# vai retornar um erro pois não conta o utimo caracter nesse caso devemos colocar o indexes 5
# isso pq o indice começa sempre do 0 
print(nome[5])
# sendo podemos pegar da seguinte forma também
print(nome[-1])

# o slice
print(nome[0:4]) # vai pegar ate o indexe 4 não incluindo o index 4 pq começa de 0
#ex R a f a e l 
#   0 1 2 3 4 5
print(nome[1: -1]) # vai do A até o E

#vamos pegar da segunda letra até a ultíma iclundo a última
print(nome[2:6])
print(nome[2:len(nome)])
print(nome[2:]) # de 2 ao infinito deixando nada apos 2: 
print(len(nome))
print(nome[:])

#passos
print(nome[0:7:2]) # pula de 2 em 2 0:1:3 0 zero e start 1 stop e o 3 step

#passo negativo
print(nome[ : : -1]) # isso e o comportamento do python nao da string
#o len chama o metodo __len__ dunderlen
#nunca use o dunderlen e sim o metodo len etc...







