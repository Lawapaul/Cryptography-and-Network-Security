def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def md5_sim(message, rounds):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    msg = bytearray(message, 'ascii')
    bit_len = len(msg) * 8
    msg.append(0x80)
    while len(msg) % 64 != 56:
        msg.append(0)
    msg += bit_len.to_bytes(8, 'little')
    for i in range(0, len(msg), 64):
        block = msg[i:i+64]
        M = [int.from_bytes(block[j*4:(j+1)*4], 'little') for j in range(16)]

        a, b, c, d = A, B, C, D

        T = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee]
        S = [7, 5, 4, 6]

        for j in range(rounds):

            if j % 4 == 0:
                f = (b & c) | (~b & d)   # F
            elif j % 4 == 1:
                f = (b & d) | (c & ~d)   # G
            elif j % 4 == 2:
                f = b ^ c ^ d            # H
            else:
                f = c ^ (b | ~d)         # I

            temp = (a + f + M[j % 16] + T[j % 4]) & 0xFFFFFFFF
            temp = left_rotate(temp, S[j % 4])
            temp = (b + temp) & 0xFFFFFFFF

        
            a, b, c, d = d, temp, b, c

        # 🔷 Add back to main hash
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # 🔷 Output
    print("After", rounds, "rounds:")
    print("A =", hex(A))
    print("B =", hex(B))
    print("C =", hex(C))
    print("D =", hex(D))


# 🔷 INPUT
msg = "SECURE123"
md5_sim(msg, 4)