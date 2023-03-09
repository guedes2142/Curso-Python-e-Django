

#for c in nome:
   # if c == 'a' or c == 'e' or c == 'i':
       # print(c.upper())

#for c in nome:
   # if c in ('a','e','i'):
        #print(c.upper())

#for c in nome:
    #if c in 'aeiou':
        #print(c.upper())
   # else:
       # print(c)
    #if c == 'u':
      #  c ='@'
        #print(c)
        
nome = 'rafael guedes'

for c in nome:

    if c in 'aeiou':
        print(c.upper())

    elif c == 'a': #TODO com if esta trocando com elif não fica a dúvida para verificar mais tarde
        print('#')

    else:
        print(c)

print(True and True) # com o and precisamos que as duas condições sejão verdaderas 
print(True and False)
print(True or True) # com o or precidamos que apenas uma seja verdadeira
print(True or False)
print(False or False) # para se queja false as 2 tem que ser falsa

 
print(True and 'abc') # retona abc pois o operador logico do python sempre retorna o ultimo elemento
#no caso do and para ele ser verdadeiro ele precisa que os 2 sejão verdadeiros

print('abc' and True) # retorna true pois ele havalia string abc que tem expressão  logica veradeira
# e depois o true retornando verdadeiro

print([] and True) # retornara lista vazia que é falso pois ele faz um curto circuito como o and exige que os
# seja iguais ele nem olha para a proxima expressão no casa seria false and true = False nesse casa o lista fazia
#e o false

print(True and []) # nessa casa e true nd false como a primeira foi verdadeira ele passou para a segunda que e false
# sendo entao que true and false é false

print(1 or []) # retorna o 1 pois como o or so exije que uma seja verdadeira ele não olha a lista vazia
# o um tem representação lógica verdadeira

print(1 or indefinido) #veja que nao estorou uma excessão pois ele nem olhou o idefinido

#print(indefinido) # retorna erro 

#print(1 and indefinido) # da erro pois o um e verdadeiro e o indefinido nem existe ele passou para verificar nesse caso
#a senguda expressão 

indefinido = True

print(1 and indefinido) # aqui retorna verdade pois indicamos que o indefinido e verdadeiro a cima com a variavel indefinido


 
        
        