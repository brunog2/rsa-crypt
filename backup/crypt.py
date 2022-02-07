import os

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
alfabeto = list('abcdefghijklmnopqrstuvwxyz '.upper())
index = [x+2 for x in range(len(alfabeto))]
#print(index)
mensagem = input("Informe a mensagem: ")

mensagemCifrada = []

for x in range(len(mensagem)):
    if mensagem[x].upper() in alfabeto:
        mensagemCifrada.append(index[alfabeto.index(mensagem[x].upper())])

#primos (p, q): 17 e 41

#n = (p - 1) * (q - 1)
#n = (17 - 1) * (41 - 1)
#e = mdc(n, x) | e == 1 | 1 < x < n

#informando as chaves que foi gerada no primeiro passo
print("Informe a chave pública da criptografia")
n = int(input("n: "))
e = int(input("e: "))

#print(mensagemCifrada)

for i in range(len(mensagemCifrada)):
    caractere = mensagemCifrada[i]
    if type(caractere) == int:
        c = (caractere**e)%n
        mensagemCifrada[i] = c    

mensagemCifrada = (" ".join([str(lst) for lst in mensagemCifrada]))

print(mensagemCifrada)

path = './public'
isExist = os.path.exists(path)

if not isExist:    
  os.makedirs(path)

try:
    arquivo = open(path+"/encrypted-text.txt", "w+")
    arquivo.write(str(mensagemCifrada))
    arquivo.close()

except:
    print("Mensagem não foi salva\n")
    