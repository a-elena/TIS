from scipy.fftpack import dct, idct  
import numpy as np

def quantize(matrix, N):
    Q = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            Q[i, j] = 20 * N * (1 + i + j)
    quantized_matrix = np.sign(matrix) * ((np.abs(matrix) // Q) * Q)
    return quantized_matrix

def naloga4(slika: np.array, velikostOkna: int) -> float:

    (H, W) = slika.shape
    nova = slika - 128
    slikaOut = np.zeros(nova.shape, dtype=np.float32)

    slikaOut = np.block([[np.clip(np.floor((idct(idct(quantize(dct(dct(nova[i:i+velikostOkna, j:j+velikostOkna], axis=0), axis=1), velikostOkna), axis=0), axis=1)) / ((2 * velikostOkna) ** 2)) + 128, 0, 255).astype(np.uint8) for j in range(0, W, velikostOkna)] for i in range(0, H, velikostOkna)])

    mse = np.mean((slika - slikaOut) ** 2)
    psnr = 20 * np.log10(255) - 10 * np.log10(mse)
    return psnr
