alfabeto = list('abcdefghijklmnopqrstuvwxyz '.upper())

class Decrypt:
    def __init__(self, text, p, q, e):
        self.text = text
        self.p = p
        self.q = q
        self.e = e
        
    def euclidesEst(self, a, b):
        r = a
        r1 = b
        u = 1
        v = 0
        u1 = 0
        v1 = 1
        while r1 != 0:
            q = int(r/r1)
            rs = r
            us = u
            vs = v
            r = r1
            u = u1
            v = v1
            r1 = rs - q * r1
            u1 = us - q * u
            v1 = vs - q * v1
        return u


    def decrypt(self):
        primesProduct = (self.p-1)*(self.q-1)
        n = self.p*self.q
        d = self.euclidesEst(self.e, primesProduct)
        
        print("d", d)
       
        decryptedText = ""

        for i in range(1, len(self.text)+1):            
            c = int(self.text[i-1])
            m = c ** d % n
            decryptedText += alfabeto[m-2]
        
        return {"decryptedText": decryptedText}
                
