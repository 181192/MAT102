# Eksempel på fullstendig bruk:
import math

from Oblig01.rsa.RSA import generate_primes, RSA_encrypt, mult_inverse, check_key


# Hjelpe metode for å oversette teksten til tabellform av tall
def string_to_num(s):
    deltab = ""
    for bokstav in s:
        bokstav = bokstav.lower()
        if bokstav.isspace():
            tall = "99"
        else:
            tall = "%.2d" % (ord(bokstav) - 97)
        deltab += tall
    return [int(deltab[x:x + 8]) for x in range(0, len(deltab), 8)]


# Hjelpe metoden for å oversette tabellform av tall til tekst
def num_to_string(s):
    res = ""
    for i in s:
        i = str(i)
        if len(i) % 2 != 0:
            i = "0" + i
        for j in range(0, len(i) - 1, 2):
            tall = i[j:j + 2]
            if tall == "99":
                res += " "
            else:
                res += chr(int(tall) + 97)
    return res


# Finne p og q, metoden returnerer en dictionary
def prim(n):
    p = 0
    primes = generate_primes(2, int(math.sqrt(n)))
    for prime in primes:
        if n % prime == 0:
            p = prime
            break
    return {'p': p, 'q': (n / p)}


# Oppgave a)
beskjed = "heisann"
n = 216541799
e = 241

T = string_to_num(beskjed)
U = RSA_encrypt(n, e, T)

# Oppgave c)
prim = prim(n)

# Oppgave d)
if not check_key(prim['p'], prim['q'], e):
    print("Check_key er false")
    exit(0)

# Oppgave e)
d = int(mult_inverse((prim['p'] - 1) * (prim['q'] - 1), e))

# Oppgave f)
dekryptert = RSA_encrypt(n, d, U)
print(num_to_string(dekryptert))

# Oppgave g)
U = [138938544, 167918735, 143648527, 162290725, 29951859, 205923221, 136395302]
dekryptert = RSA_encrypt(n, d, U)
print(num_to_string(dekryptert))
