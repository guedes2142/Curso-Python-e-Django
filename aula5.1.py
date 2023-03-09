nome = 'rafael'.encode()
print(nome) # b'rafael'
nomeb = 'rafaél'.encode()
print(nomeb)# b'rafa\xc3\xa9l'

#string no python não e uma sequincia de bytes na memoria, string são objetos de auto nivel que implementa toda
#complexidade do unicode
#string no python são imútaveis vc não consegue mudar um caracter dentro da string
#qualquer operação dentro daquela string me retorna uma nova copia daquela string

nomez = 'rafael'.capitalize()
print(nomez)
nomea ='rafael'.title()
print(nomea)
nomec = 'rafael'.replace('a', '4').title()
print(nomec)
nomev = 'rafael guedes'.split() # me retorna o nome separado em uma lista de strings
print(nomev)
nomex = 'rafael guedes'.split('a') # consome a letra a, não consome o espaço
print(nomex)
#concatenar é simples

nomen = 'rafael'
nomem = 'guedes'

concatenado = nomen + nomem
print(concatenado)
#ou assim
print('rafael'+' '+'guedes') # esteme metodos não e muito simples para uma lista com varias strings
                             #neste caso podemos usar metodo join
# ' .join([])e passamos a lista para dentro do join exemplo de string

mtdjoin = ' '.join(['Rafael', 'Guedes', 'De', 'Almeida'])
print(mtdjoin, ':este é o metodo join')
# outro exemplo e usar '\n' para criar linhas
mtdjoin2 = '\n'.join(['Rafael', 'Guedes', 'De', 'Almeida'])
print(mtdjoin2)
# saber o comprimento da string usando o função len
nomeq = 'rafael guedes de almeida'
nomeqlen =len(nomeq)
print(f'{nomeq} contem: {nomeqlen} caracteres')
