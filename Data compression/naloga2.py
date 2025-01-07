def naloga2(vhod: list, nacin: int) -> tuple[list, float]:

    izhod = []
    R = float('nan')

    if(nacin == 0):
        slovar = {chr(i): i for i in range(256)}
        
        N = ""         
        
        stVnos = 256       
        maxVnos = 4096

        for c in vhod:
            NZ = N + c
            if NZ in slovar:
                N = NZ
            else:
                izhod.append(slovar[N])
                if stVnos < maxVnos:
                    slovar[NZ] = stVnos
                    stVnos += 1
                N = c
        if N:
            izhod.append(slovar[N])
        R = (len(vhod) * 8) / (len(izhod) * 12)

    else:
        slovar = {i: chr(i) for i in range(256)}
        
        stVnos = 255
        maxVnos = 4096

        k = vhod[0]
        N = slovar[k]
        niz = ''
        niz += N
        K = N

        for i in range(1, len(vhod)):
            k = vhod[i]
            
            if k in slovar:
                N = slovar[k]
            else:
                N = K + K[0]
            
            niz += (N)
            
            if stVnos < maxVnos:
                stVnos += 1
                slovar[stVnos] = K + N[0] 
            
            K = N
        izhod = list(niz)
        R = (len(izhod) * 8) / (len(vhod) * 12)


    return (izhod, R)
