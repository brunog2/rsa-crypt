#essa class será utilizada para gerar as chaves publicas
#para criptografia 

from contextlib import nullcontext
from operator import truediv
import random
import os

def primesInRange(p,q):
    primes_List = []
    for n in range(p,q):
        isPrime = True

        for num in range(2,n):
            if n % num == 0:
                isPrime = False
        
        if isPrime:
            primes_List.append(n)
    
    return primes_List

def MDC(p,q,e):
    primes_list = []
    for n in range(2,e):
        isCoPrime = True
        if n%p == 0 or n%q == 0:
            isCoPrime = False
        if isCoPrime:
            primes_list.append(n)
        
    return primes_list


#inserção de dados para gerar as chaves publicas

print("Informe dois numeros primos:\n")

p = int(input('Insira o 1° valor: '))
q = int(input('Insira o 2° valor: '))

#recupera a lista de numeros primos
#primes_list = primesInRange(p,q)

#seleciona os numeros primos de forma aleatória 
#keyOne = random.choice(primes_list)
#keyTwo = random.choice(primes_list)

#verifica e garante que as chaves não são iguais

#while keyOne == keyTwo:
#    keyTwo = random.choice(primes_list)

#calculo do exponencial para a criptografia
n = p*q

#selecionando um expoente relativamente primo a (p-1)*(q-1) 
#aleatoriamente
print("\nDeseja gerar um expoente aleatoriamente ou digitar manualmente?\n")
generateE = input("1 - Gerar expoente | 2 - Digitar manualmente: ")
e = None
if generateE != str(1):
    e = int(input("\nDigite um número qualquer relativamente primo a {}: ".format((p-1)*(q-1))))
    while e%p == 0 or e%q == 0:
        print("O número informado não é relativamente primo a {}!".format((p-1)*(q-1)))
        e = int(input("\nDigite um número qualquer relativamente primo a {}: ".format((p-1)*(q-1))))
else:        
    coPrimes_list = MDC(p,q,(p-1)*(q-1))
    print(coPrimes_list)
    e = random.choice(coPrimes_list)

    #caso não seja permitido gerar um coprimo aleatoriamente
    #pedindo ao usuário

#informar as chaves para a descriptografia
#print("\nAnote a chave para criptografar a mensagem")
print("\nA chave pública é: ({}, {})".format(n, e))
print("Anote os primos digitados! Eles servirão para descriptografar a mensagem.")
#informa a chave para a descriptografia ao usuário

#print("\nanote suas chaves para descriptografar a mensagem")
#print("sua primeira chave é: ",keyOne)
#print("sua segunda chave é: ",keyTwo)
#print("sua terceira chave é: ",e)

#adiciona as chaves publica no arquivo txt


#try:
#    writeKey("a")

#except FileNotFoundError:
#    writeKey("w+")

#ao gerar uma nova chave pública, o que estiver dentro do arquivo
#deve ser substituído

path = './publicKey'
isExist = os.path.exists(path)

if not isExist:    
  os.makedirs(path)

arquivo = open(path+"/KeyPublic.txt", "w+")
arquivo.write(str(n)+"\n")
arquivo.write(str(e)+"\n")
arquivo.close()