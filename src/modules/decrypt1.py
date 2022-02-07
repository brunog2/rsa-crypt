alfabeto = list('abcdefghijklmnopqrstuvwxyz '.upper())

class Decrypt:
    def __init__(self, text, p, q, e):
        self.text = text
        self.p = p
        self.q = q
        self.e = e
        
  
    def decrypt(self):
        k = 0
        d = self.p * self.q
        m = (self.p-1)*(self.q-1)
        a = self.e%m
        for x in range(1, m):
            if ((a*x) % m == 1):
                k = x
        decryptedText = ""

        for i in range(1, len(self.text)+1):
            k1 = k
            n = int(self.text[i-1])
            pot = n % d
            
            result = 1
            
            
            while int(k1) > 0:
                if int(k1) % 2 == 1:
                    result = (result * pot) % d
                    
                pot = (pot * pot) % d
                k1 /= 2

            decryptedText += alfabeto[result-2]
        
        return {"decryptedText": decryptedText}
                
