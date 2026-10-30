def right_rotate(x,n):
    return ((x>>n) | (x << (64-n))) & 0xFFFFFFFFFFFFFFFF

def sha_512(msg,rounds):
    initial = [
        0x6a09e667f3bcc908, 0xbb67ae8584caa73b,
        0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
        0x510e527fade682d1, 0x9b05688c2b3e6c1f,
        0x1f83d9abfb41bd6b, 0x5be0cd19137e2179
    ]
    k = [
        0x428a2f98d728ae22,
        0x7137449123ef65cd,
        0xb5c0fbcfec4d3b2f
    ]
    msg = bytearray(msg,'ascii')
    bit_len = len(msg) * 8
    msg.append(0x80)
    while((len(msg)*8) % 1024 != 896):
        msg.append(0)
    msg+=bit_len.to_bytes(16,'big')
    for i in range(0,len(msg),128):
        block = msg[i:i+128]
        w=[]
        for j in range(16):
            w.append(int.from_bytes(block[j*8:(j+1)*8],'big'))
        for j in range(16):
            w.append(0)
        a,b,c,d,e,f,g,h = initial
        for j in range(rounds):
            s1 = right_rotate(e,14) ^ right_rotate(e,18) ^ right_rotate(e,41)
            ch = (e&f) ^ (~e & g)
            t1 = (h + a + ch + w[j] + s1 + k[j%len(k)]) & 0xFFFFFFFFFFFFFFFF
            
            s0 = right_rotate(a,28) ^ right_rotate(a,34) ^ right_rotate(a,39)
            maj = (a&b) ^ (b&c) ^ (c&a)
            t2 = (s0 + maj) & 0xFFFFFFFFFFFFFFFF
            h = g
            g = f
            f = e
            e = (d + t1)&0xFFFFFFFFFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFFFFFFFFFF
        initial[0] = (initial[0] + a) & 0xFFFFFFFFFFFFFFFF
        initial[1] = (initial[1] + b) & 0xFFFFFFFFFFFFFFFF
        initial[2] = (initial[2] + c) & 0xFFFFFFFFFFFFFFFF
        initial[3] = (initial[3] + d) & 0xFFFFFFFFFFFFFFFF
        initial[4] = (initial[4] + e) & 0xFFFFFFFFFFFFFFFF
        initial[5] = (initial[5] + f) & 0xFFFFFFFFFFFFFFFF
        initial[6] = (initial[6] + g) & 0xFFFFFFFFFFFFFFFF
        initial[7] = (initial[7] + h) & 0xFFFFFFFFFFFFFFFF
    return ''.join(format(x,'016x') for x in initial)

msg = input("Enter Message: ")
print(sha_512(msg,3))