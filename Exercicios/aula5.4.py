#tuplas

nome = ('rafael guedes de almeida')
nome = tuple(nome)
print(nome)

t = nome
print(t[0], t[1], t[2])

nome_reverso = nome[::-1]

print(nome_reverso)

for i in nome_reverso:
    print(i)