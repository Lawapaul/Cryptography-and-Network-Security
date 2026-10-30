def mod_inv(x,q):
    for i in range(1,q):
        if(i*x) % q==1:
            return i

q = 997
g = 5
private_key = []
public_key = []
n = int(input("Enter no of Users: "))
for i in range(n):
    x = int(input(f"Enter Private Key of user {i+1}: "))
    private_key.append(x)
    public_key.append(pow(g,x,q))

shared = 1
for j in public_key:
    shared = (shared*j) % q

#Encryption
msg = input("Enter Message: ")
msg = bytearray(msg,'ascii')
ct = []
for byte in msg:
    ct.append((byte*shared) % q)
v= mod_inv(shared,q)
pt = ''.join(chr((i*v) % q) for i in ct)
print("Plain Text: ",pt)