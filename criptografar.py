# import os

# --chave publica--
# solicitar 2 numeros primos p e q e um expoente relativamente primo a (p - 1)(q - 1).
# salvar num arquivo os dois números primos | (?expoente?)

# --encriptar--
# solicitar texto a ser encriptado
# solicitar a chave publica que o usuario recebeu
# salvar em um arquivo a mensagem criptografada

# --desencriptar--
# solicitar p,q, e ao usuario
# salvar a mensagem desencriptada em um arquivo

# A mensagem deve ser encriptada usando o alfabeto de letras A - Z,
# codificado com inteiros de 2 a 28, onde 2 = A, 3 = B,..., 27 = Z, 28 = espaço
mensagem = input("Informe a mensagem: ")
alfabeto = list('abcdefghijlmnopqrstuvxz'.upper())
index = [x+1 for x in range(len(alfabeto))]
#print(index)
mensagemCifrada = []

for x in range(len(mensagem)):
    mensagemCifrada.append(index[alfabeto.index(mensagem[x].upper())])

#primos (p, q): 17 e 41

#n = (p - 1) * (q - 1)
#n = (17 - 1) * (41 - 1)
#e = mdc(n, x) | e == 1 | 1 < x < n

p, q = 17, 41

#Chave pública = (n, e)
#Chave pública = (697, 13)
n = p*q
e = 13

#print(mensagemCifrada)

for i in range(len(mensagemCifrada)):
    caractere = mensagemCifrada[i]
    c = (caractere**e)%n
    mensagemCifrada[i] = c

print(mensagemCifrada)