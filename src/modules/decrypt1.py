alfabeto = list('abcdefghijklmnopqrstuvwxyz '.upper())

class Decrypt:
    def __init__(self, text, p, q, e):
        self.text = text
        self.p = p
        self.q = q
        self.e = e
        
    def euclidesEst(self, a, b, c):
        r = abs(a%b)
        print("r", r)
        if r == 0:
            print("r 0", abs((c/a)%(b/a)))
            return int(abs((c/a)%(b/a)))
        return int((self.euclidesEst(r, a, -c)) * ((b + c / abs(a%b))))

    def decrypt(self):
        primesProduct = (self.p-1)*(self.q-1)
        n = self.p*self.q
        d = self.euclidesEst(self.e, primesProduct, 1)
        
        print("d", d)
       
        decryptedText = ""

        for i in range(1, len(self.text)+1):            
            n = int(self.text[i-1])
            m = (n ^ d ) % n
            decryptedText += alfabeto[m-2]
        
        return {"decryptedText": decryptedText}
                
