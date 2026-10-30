import socket

def gcd(a,b):
    while(b):
        a,b = b,a%b
    return a

def inv_mod(e,phi):
    for i in range(1,phi):
        if (e*i)%phi ==1:
            return i

p = 61
q = 53
n = p*q
phi = (p-1)*(q-1)
e = 17
d = inv_mod(e,phi)

server = socket.socket()
server.bind(("localhost",12345))
server.listen(1)

conn,addr = server.accept()
conn.send(f"{e} {n}".encode())

data = conn.recv(1024).decode()
cipher = list(map(int, data.split()))
message = ""
for c in cipher:
    message+= chr(pow(c,d,n))
print("Decrypted Message: ",message)
conn.close()
server.close()