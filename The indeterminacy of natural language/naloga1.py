from math import log2
from collections import Counter


def naloga1(besedilo: str, p: int) -> float:

    B="".join(filter(str.isalpha,besedilo)).upper()
    N=len(B)
    H = float("nan")

    B0=list(B[:])
    B1=list(B[1:])
    B2=list(B[2:])
    B3=list(B[3:])

    if (p == 0):
        freq1=Counter(B)
        H0=sum(-(freq1[k]/N)*log2(freq1[k]/N) for k in freq1)   

        H=H0

    elif (p == 1):
        freq1=Counter(B)
        H0=sum(-(freq1[k]/N)*log2(freq1[k]/N) for k in freq1)

        pairs2=list(zip(B0,B1))
        freq2=Counter(pairs2)
        H1=sum(-(freq2[k]/(N-1))*log2(freq2[k]/(N-1)) for k in freq2)

        H=H1-H0

    elif (p == 2):
        pairs2=list(zip(B0,B1))
        freq2=Counter(pairs2)
        H1=sum(-(freq2[k]/(N-1))*log2(freq2[k]/(N-1)) for k in freq2)

        pairs3=list(zip(B0,B1,B2))
        freq3=Counter(pairs3)
        H2=sum(-(freq3[k]/(N-2))*log2(freq3[k]/(N-2)) for k in freq3)

        H=H2-H1

    elif (p == 3):
        pairs3=list(zip(B0,B1,B2))
        freq3=Counter(pairs3)
        H2=sum(-(freq3[k]/(N-2))*log2(freq3[k]/(N-2)) for k in freq3)

        pairs4=list(zip(B0,B1,B2,B3))
        freq4=Counter(pairs4)
        H3=sum(-(freq4[k]/(N-3))*log2(freq4[k]/(N-3)) for k in freq4)

        H=H3-H2

    return H
