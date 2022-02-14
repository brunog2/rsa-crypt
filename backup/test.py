def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

a = 2466792710041573976620363854606408339652968288291266805622075100148322903846195042164762626226715891
m = 11469490193260527966549948187682837924164162368980523943492391879744673143905669725550385666101872381929414509592048151269690849248987210517234214209160961754050838745200598254335368730962661500037423

try:
    res=modinv(a,m)
    print("The required modular inverse is: "+ str(res))

except:
    print('The modular inverse does not exist.')