# 🔷 GF multiplication (general)
def mul(x, y):
    r = 0
    for _ in range(8):
        if y & 1:
            r ^= x
        hi = x & 0x80
        x = (x << 1) & 0xFF
        if hi:
            x ^= 0x1B
        y >>= 1
    return r

# 🔷 Convert hex → matrix (column-wise)
def hex_to_matrix(h):
    b=[int(h[i:i+2],16) for i in range(0,32,2)]
    return [[b[r+4*c] for c in range(4)] for r in range(4)]

# 🔷 AddRoundKey
def addkey(s,k):
    return [[s[i][j]^k[i][j] for j in range(4)] for i in range(4)]

# 🔷 InvShiftRows
def inv_shift(s):
    s[1]=s[1][-1:]+s[1][:-1]
    s[2]=s[2][-2:]+s[2][:-2]
    s[3]=s[3][-3:]+s[3][:-3]
    return s

# 🔷 InvMixColumns
def inv_mix(s):
    r=[[0]*4 for _ in range(4)]
    for j in range(4):
        r[0][j]=mul(s[0][j],14)^mul(s[1][j],11)^mul(s[2][j],13)^mul(s[3][j],9)
        r[1][j]=mul(s[0][j],9)^mul(s[1][j],14)^mul(s[2][j],11)^mul(s[3][j],13)
        r[2][j]=mul(s[0][j],13)^mul(s[1][j],9)^mul(s[2][j],14)^mul(s[3][j],11)
        r[3][j]=mul(s[0][j],11)^mul(s[1][j],13)^mul(s[2][j],9)^mul(s[3][j],14)
    return r

# 🔷 InvSubBytes (if inverse S-box given)
def inv_sub_bytes(s, inv_sbox):
    return [[inv_sbox[val>>4][val&0x0F] for val in row] for row in s]

def aes_decrypt_n_rounds(ciphertext, key_hex, n, inv_sbox=None):

    s = hex_to_matrix(ciphertext)
    key = hex_to_matrix(key_hex)

    # 🔷 Final round first (reverse)
    s = addkey(s, key)
    s = inv_shift(s)
    if inv_sbox:
        s = inv_sub_bytes(s, inv_sbox)

    # 🔷 Rounds n-1 → 1
    for r in range(n-1, 0, -1):
        s = addkey(s, key)
        s = inv_mix(s)
        s = inv_shift(s)
        if inv_sbox:
            s = inv_sub_bytes(s, inv_sbox)

    # 🔷 Round 0
    s = addkey(s, key)

    return s


# 🔷 Example usage
cipher = "87EC4A8CF26EC3D84D4C46959790E7A6"
key = "000102030405060708090A0B0C0D0E0F"

result = aes_decrypt_n_rounds(cipher, key, n=4)

print("Decrypted State:")
for row in result:
    print(*[f"{x:02X}" for x in row])