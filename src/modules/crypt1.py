import unidecode

alfabeto = list('abcdefghijklmnopqrstuvwxyz '.upper())
index = [x+2 for x in range(len(alfabeto))]

class Crypt:
    def __init__(self, text, n, e):
        self.text = unidecode.unidecode(text)
        self.n = int(n)
        self.e = int(e)
        
    def expModular(self, c, d, n):
        #m1 = c ** d % n
        m = 1
        pot = c % n
        while (int(d) > 0):
                print("d (while):", int(d))
                if (int(d) % 2 == 1):
                    print("resultado ({} * {}) % {} = {}".format(int(m), int(pot), int(n), (int(m) * int(pot)) % int(n)))
                    m = (int(m) * int(pot)) % int(n)
                pot = (int(pot) * int(pot)) % int(n)
                d /= 2
        return m

    def crypt(self):
        mensagemCifrada = []

        for x in range(len(self.text)):
            if self.text[x].upper() in alfabeto:
                mensagemCifrada.append(index[alfabeto.index(self.text[x].upper())])

        for i in range(len(mensagemCifrada)):
            caractere = mensagemCifrada[i]
            if type(caractere) == int:
                #c = (caractere ** self.e) % self.n
                c = self.expModular(caractere, self.e, self.n)
                mensagemCifrada[i] = c    

        mensagemCifrada = (" ".join([str(lst) for lst in mensagemCifrada]))
        return {"encryptedText": mensagemCifrada}