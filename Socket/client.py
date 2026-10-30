import socket
client = socket.socket()
client.connect(("localhost",12345))
data = client.recv(1024).decode()

message = input("Enter the message to encrypt: ")
e, n = map(int, data.split())
ct = ""
for c in message:
    ct += str(pow(ord(c), e, n)) + " "
client.send(ct.encode())
client.close()