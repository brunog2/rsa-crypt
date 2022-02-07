from contextlib import nullcontext
from operator import truediv
from math import gcd
import random
import os

class Gen:
    def __init__(self, p, q, e = None):
        self.p = p
        self.q = q
        self.e = e

    def prime(self):
        maior = self.p
        if self.p < self.q:
            maior = self.q

        for x in range(2, maior):
            if (x != self.p and x != self.q) and (self.p % x == 0 or self.q % x == 0):
                return False
        return True

    def gen(self):
        primesProduct = (self.p-1)*(self.q-1)
        print("mdc", gcd(self.e, primesProduct))
        if not self.prime():
            return {"message": "Número informado não é primo!"}
        if self.e == None:
            return {"message": "Expoente não informado!"}
        if self.e > (self.p - 1) * (self.q - 1):
            return {"message": "Expoente maior que o produto!"}
        if gcd(self.e, primesProduct) != 1:
            return {"message": "O número não é relativamente primo!"}
        else:
            return {"n": self.p * self.q, "e": self.e}
