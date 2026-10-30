p = 23
q = 11
x = 5
hm = sum(bytearray("Auth",'ascii')) % q
h = 2
g = pow(h, (p-1)//q, p)
k = 2
def mod_inv(k,q):
    for i in range(1,q):
        if (k*i) % q == 1:
            return i

public_key = pow(g, x, p)
r = pow(g, k, p) % q
s = (mod_inv(k,q) * (hm + x*r)) % q 
print(f"DSA Component: ({r},{s})")

w = mod_inv(s,q)
u1 = (hm*w) % q
u2 = (r*w) % q

v = (pow(g,u1,p) * pow(public_key,u2,p) % p) % q

print("v =", v)
print("r =", r)

if v == r:
    print("Signature VALID ✅")
else:
    print("Signature INVALID ❌")