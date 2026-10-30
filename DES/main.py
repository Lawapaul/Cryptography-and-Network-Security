def permutate(bits,n):
    return "".join([bits[i-1] for i in n])

def xor(a,b):
    result = ""
    for i in range(len(a)):
        result+=str(int(a[i]) ^ int(b[i]))
    return result

def shift(bits,n):
    return bits[n:] + bits[:n]

def swap(bits):
    return bits[4:]+bits[:4]

def generate_keys(key):
    P10 = [3,5,2,7,4,10,1,9,8,6]
    P8 = [6,3,7,4,8,5,10,9]
    bits = permutate(key,P10)
    left,right = bits[:5],bits[5:]
    left_shift,right_shift = shift(left,1),shift(right,1)
    k1 = permutate(left_shift + right_shift,P8)
    left_shift,right_shift = shift(left_shift,2),shift(right_shift,2)
    k2 = permutate(left_shift + right_shift,P8)
    return k1,k2

s0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
s1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def fk(bits,key):
    EP = [4,1,2,3,2,3,4,1]
    P4 = [2,4,3,1]
    left,right = bits[:4],bits[4:]
    bits = permutate(right,EP)
    xored = xor(key,bits)
    left_xored = xored[:4]
    right_xored = xored[4:]
    row = int(left_xored[0] + left_xored[3],2)
    col = int(left_xored[1] + left_xored[2],2)
    s0_val = format(s0[row][col],"02b")
    row = int(right_xored[0] + right_xored[3],2)
    col = int(right_xored[1] + right_xored[2],2)
    s1_val = format(s1[row][col],"02b")
    
    combined = permutate(s0_val + s1_val,P4)
    left_part = xor(left,combined)
    return left_part + right
    
def encrypt(msg,key):
    IP = [2,6,3,1,4,8,5,7]
    IP_INV = [4,1,3,5,7,2,8,6]
    k1,k2 = generate_keys(key)
    bits = permutate(msg,IP)
    bits = fk(bits,k1)
    bits = swap(bits)
    bits = fk(bits,k2)
    ct = permutate(bits,IP_INV)
    return ct

def decrypt(ct,key):
    IP = [2,6,3,1,4,8,5,7]
    IP_INV = [4,1,3,5,7,2,8,6]
    k1,k2 = generate_keys(key)
    bits = permutate(ct,IP)
    bits = fk(bits,k2)
    bits = swap(bits)
    bits = fk(bits,k1)
    ct = permutate(bits,IP_INV)
    return ct
    
pt = "10111101"
key = "1010000010"
ct = encrypt(pt,key)
print("Cipher Text: ",ct)

pt = decrypt(ct,key)
print("Plain Text: ",pt)