
def mod_inv(e,phi):
    for i in range(1,phi):
        if(e*i) % phi ==1:
            return i
            
p = 17
q = 11
M = 88

e = 7
n = p*q
phi = (p-1) * (q-1)

print(f"public key ({e},{n})")
d = mod_inv(e,phi)
print(f"private key ({d},{n})")

ct = pow(M,e,n)
print("Cipher Text: ",ct)
pt = pow(ct,d,n)
print("Plain Text: ",pt)
