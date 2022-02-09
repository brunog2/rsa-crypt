from math import gcd
import random
from this import d

class Gen:
    def __init__(self, p, q, e = None):
        self.p = p
        self.q = q
        self.e = e

    # realiza a potencia dos números para o teste de rabin
    def power(self, x, y, p):         
        res = 1        
        x = x % p
        while (y > 0):
            if (y & 1):
                res = (res * x) % p
            y = y>>1
            x = (x * x) % p
        return res
 
    # executa o teste de rabin com um inteiro d obtido por uma expressão
    # e um n a qual se deseja verificar primalidade
    def testeRabin(self, d, n):
        a = 2 + random.randint(1, n - 4)    
        x = self.power(a, d, n)
    
        if (x == 1 or x == n - 1):
            return True
  
        while (d != n - 1):
            x = (x * x) % n;
            d *= 2
    
            if (x == 1):
                return False
            if (x == n - 1):
                return True

        return False
 
    # funcao que faz o teste de primalidade de rabin k vezes
    # quanto maior o k, maior a precisão do teste
    def primo(self, n, k):
        if (n <= 1 or n == 4):
            return False
        if (n <= 3):
            return True

        d = n - 1;
        while (d % 2 == 0):
            d //= 2
    
        for i in range(k):
            if (self.testeRabin(d, n) == False):
                return False
    
        return True

    # algoritmo de euclides simples
    # para extrair o mdc
    def euclides(self, a, b):
        if a == b: return b
        elif a > b:
            if a % b == 0: return b
            else: return self.euclides(b, a % b)
        else:
            if b % a == 0: return a
            else: return self.euclides(a, b % a)

    def gen(self):
        primesProduct = ((self.p-1)*(self.q-1)) // 1
        print("prim ", primesProduct)
        print("e ", self.e)
        print("mdc", self.euclides(self.e, primesProduct))
        if not self.primo(self.p, 4) or not self.primo(self.q, 4):
            return {"message": "Número informado não é primo!"}
        if self.e == None:
            return {"message": "Expoente não informado!"}
        if self.e > (self.p - 1) * (self.q - 1):
            return {"message": "Expoente maior que o produto!"}
        if self.euclides(self.e, primesProduct) != 1:
            return {"message": "O número não é relativamente primo!"}
        else:
            return {"n": (self.p * self.q) // 1, "e": self.e}
