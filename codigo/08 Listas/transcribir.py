# -*- coding: utf-8 -*-

import string

# Ahora podemos hacer bioinformática!



def transcribir(secuenciaDNA):
    secuenciaRNA = []
    for nucleotido in secuenciaDNA:
        if nucleotido=='T':
            secuenciaRNA.append('U')
        else:
            secuenciaRNA.append(nucleotido)
    return secuenciaRNA

DNA1 = "AGGCTGAATAGCTTTATCAGATTCGGTGTGTTTAGGCTAGCTTTCCTGATTTTGCATCAAAGCTTAATTGATAAAGCATCGGCTGCCTACCTCCTGTGCCCATAGATCTAACTTGCGGTCTTTATCTATAGGCTCTCAAGCAAGTGCCTCGCGATATGCTATTGATCAGAGGCCTCTCGAAGGGAGTTATTTTGTTTATGCCCAAACTGCACGCATCCTCGCTCCGCGCCCTCTTTAATGTGCTAGCATCCCAGTTCTCAGGCTCTATATCGCCGCCTGTCCGTTAAAAACTAGCTTTATGTTCGAGGATTTTTCGTGTGTTTAGCAGCTGGTTCGGGGGCTGGACACCATAGGCTTGAGTAGCCATATCAGTCTACCACGCTTCACGTGTTGACCTGCTTGGCCCCTTTGGTTCTTGTTATCCCGCAGGTGGGGTGTGCCGATCTACCATCGTTCGTGCGCGTTGGATTGAGGTACCATACCAAAATATTTACTAGAGCGATGTGGTACTAGAAGCTACTATAGAGCGTGTCTCAGCGTATCCGGGGACACAGTGTGATTGCTTAAAGGAATCTCTCCGCTCCTCCCCAGGAGATCCAGTTGCTAGTTCAGATCGAGAAACGGGGTCTCAACAGAGGTGAGCGGACTCGCCCGTCGAAAAGACTCTGTGTAATCATAGTGAACGAGCCCCTCAAGTTGAAAACGTTGTGAATAATACACTATGCAGCATCTCTTGGGGTCATTACGCCGATAGCGGCAGCCGGTTGCAATAATCTGGCTGACTAAATCCTACACGGAGGAGGATGTAGGGAAAGATGTCCTACGG"

RNA1 = transcribir(DNA1)

print(RNA1)
print(str.join("",RNA1))
