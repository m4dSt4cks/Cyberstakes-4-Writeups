Zimport binascii

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

def big_exponent(base, exp, mod):
    answer = 1
    while exp > 0:
        if exp % 2 == 0:
            base = (pow(base, 2)) % mod
            exp /= 2
        else:
            answer = (base * answer) % mod
            exp -= 1
    return answer

c = 0x1a7627ccc36d251fb9276fb3d312807409e6a486ba2cbbd94d4e35d74dc29dda
p = 331958624987283540029528593686625501199
q = 368413955753084554445712063216091990363
e = 65537

totient = (p - 1) * (q - 1)
d = modinv(e, totient)
flag = big_exponent(c, d, p * q)
print(binascii.unhexlify(hex(flag).rstrip("L").lstrip("0x")))

# https://www.alpertron.com.ar/ECM.HTM
