alfabeto = list('abcdefghijklmnopqrstuvwxyz '.upper())
index = [x+2 for x in range(len(alfabeto))]

class Crypt:
    def __init__(self, text, n, e):
        self.text = text
        self.n = n
        self.e = e
        
    def crypt(self):
        mensagemCifrada = []

        for x in range(len(self.text)):
            if self.text[x].upper() in alfabeto:
                mensagemCifrada.append(index[alfabeto.index(self.text[x].upper())])

        for i in range(len(mensagemCifrada)):
            caractere = mensagemCifrada[i]
            if type(caractere) == int:
                c = (caractere ** self.e) % self.n
                mensagemCifrada[i] = c    

        mensagemCifrada = (" ".join([str(lst) for lst in mensagemCifrada]))
        return {"encryptedText": mensagemCifrada}