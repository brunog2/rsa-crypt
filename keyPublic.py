#essa class será utilizada para gerar as chaves publicas
#para criptografia 

from operator import truediv
import random

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

print("Informe dois numeros inteiros e distintos com diferença minima de 100 numeros para gerar a chave de criptografia:\n")

p = int(input('insira o 1° valor:'))
q = int(input('insira o 2° valor:'))

#recupera a lista de numeros primos
primes_list = primesInRange(p,q)

#seleciona os numeros primos de forma aleatória 
keyOne = random.choice(primes_list)
keyTwo = random.choice(primes_list)

#verifica e garante que as chaves não são iguais

while keyOne == keyTwo:
    keyTwo = random.choice(primes_list)

#calculo do exponencial para a criptografia
e = (keyOne-1)*(keyTwo-1)

coPrimes_list = MDC(keyOne,keyTwo,e)

e = random.choice(coPrimes_list)

#informar as chaves para a descriptografia
print("anote suas chaves para criptografar a mensagem\n")
print("primeira chave é: ",(keyOne*keyTwo),"\n")
print("segunda chave é: ",e,"\n")

#informa a chave para a descriptografia ao usuário

print("anote suas chaves para descriptografar a mensagem\n")
print("sua primeira chave é: ",keyOne,"\n")
print("sua segunda chave é: ",keyTwo,"\n")
print("sua terceira chave é: ",e,"\n")

#adiciona as chaves publica no arquivo txt
try:
    arquivo = open("keyFolder/KeyPublic.txt","a")
    arquivo.write(keyOne,"\n")
    arquivo.write(keyTwo,"\n")
    arquivo.write(e,"\n")
    arquivo.close()

except FileNotFoundError:
    arquivo = open("keyFolder/KeyPublic.txt","w+")
    arquivo.write(keyOne,"\n")
    arquivo.write(keyTwo,"\n")
    arquivo.write(e,"\n")
    arquivo.close()

