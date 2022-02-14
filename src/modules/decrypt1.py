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
        #print("m: 21 22 19 10 15 8")
        primesProduct = (self.p-1)*(self.q-1)
        n = self.p*self.q
        #d1 = abs(self.euclidesEst(self.e, primesProduct))   # <- errado
        # d1 = pow(self.e, -1, primesProduct) # <-  certo
        
        d1 = 87274316104749024
        print("e ",(self.e))
        print("n ",primesProduct)
        print("inv ",(d1))
       
        decryptedText = ""

        for i in range(1, len(self.text)+1):      
            d = d1
            #print("d, i", d, i)
            c = int(self.text[i-1])
            #m1 = c ** d % n
            #print(c, d, n)
            m = 1
            pot = c % n
            
            #print("pot: {} % {} = {}".format(c, n, pot))
            while (int(d) > 0):
             #   print("d (while):", int(d))
                if (int(d) % 2 == 1):
                    #print("resultado ({} * {}) % {} = {}".format(int(m), int(pot), int(n), (int(m) * int(pot)) % int(n)))
                    m = (int(m) * int(pot)) % int(n)
                pot = (int(pot) * int(pot)) % int(n)
                d /= 2

            #print("c, m (pre), m (obt)", c, m)   
            print("m", m)
            decryptedText += alfabeto[m-2]
        
        return {"decryptedText": decryptedText}
                
