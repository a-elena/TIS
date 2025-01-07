import numpy as np
from math import log2

def naloga3(vhod: list, n: int) -> tuple[list, str]:

    izhod = []
    

    index1 = 0
    brKodovi = int(len(vhod) / n)
    matrix = []
    for x in range(brKodovi):
        vrsta = []
        for y in range(n):
            vrsta.append(vhod[index1])
            index1 = index1 + 1
        matrix.append(vrsta)
   

    for i in range(brKodovi):
        z=np.array(matrix[i], dtype=np.uint8)
        vhodI = matrix[i]
        
        varBiti = int(log2(n) + 1)
        
        koda = n - varBiti
        
        mH = varBiti - 1
        parity = np.remainder(np.sum(z),2)
       
        nH = n-1
        H = []
        for i in range(1, n):
            if log2(i) % 1 != 0:
                bin_str = bin(i)[2:]
                padded_str = bin_str.zfill(mH)
                broj = [int(digit) for digit in padded_str]
                H.append(broj)
        #print(H)
        H = np.transpose(np.array(H))
        #print("transponirana\n")
        #print(H)
        H = np.concatenate((H, np.eye(H.shape[0], dtype=int)), axis=1)

        vlez1 = np.array(vhodI[:-1], dtype=np.uint8)
        sindrom = vlez1.dot(np.transpose(H))
        sindrom=np.remainder(sindrom,2)
        
        index = np.where(np.apply_along_axis(lambda x: np.array_equal(x, sindrom), 0, H))[0]

        e = np.zeros(nH)
        e = np.array(e, dtype=np.uint8)
        e[index] = 1
       
        if parity == 0:
            if np.all(sindrom == 0):
                
                for x in range(koda):
                    izhod.append(vlez1[x])
            else:
                for x in range(koda):
                    izhod.append(vlez1[x])
        if parity == 1:
            if np.all(sindrom == 0):
                
                for x in range(koda):
                    izhod.append(vlez1[x])
            else:
                vlez1 = vlez1 ^ e
                for x in range(koda):
                    izhod.append(vlez1[x])


    crc = ''
    reg = [1,1,1,1,1,1,1,1] 
    regPr = reg.copy()

    for x in range(len(vhod)):
        regPr = reg.copy()

        pm = (vhod[x] ^ regPr[0])
        if pm == 0:
            for y in range(7):
                reg[y] = regPr[y + 1]
            reg[7] = pm
        if pm == 1:
            for y in range(7):
                reg[y] = regPr[y + 1]
            reg[7] = pm
            reg[0] = int(not reg[0])
            reg[3] = int(not reg[3])
            reg[4] = int(not reg[4])
            reg[6] = int(not reg[6])
    
    binary_string = ''.join(str(bit) for bit in reg)
    binary_int = int(binary_string, 2)
    hex_string = hex(binary_int)[2:]
    crc = hex_string.zfill(2)

    return (izhod, crc)


