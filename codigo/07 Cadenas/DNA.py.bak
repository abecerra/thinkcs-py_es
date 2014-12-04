# -*- coding: utf-8 -*-

# Ahora podemos hacer bioinformática!



def nucleotidoValido(n):
  return n =='A' or n=='C' or n=='T' or n=='G'
    
def esCadenadeDNA(secuencia):
  for nucleotido in secuencia:
    if not nucleotidoValido(nucleotido):
      return False
  return True

def contarNucleotidos1(secuencia):
    A = C = G = T = 0
    j = 0
    while j< len(secuencia):
        if secuencia[j] == 'A':
            A = A+1
        if secuencia[j] == 'C':
            C =  C+1
        if secuencia[j] == 'G':
            G = G+1
        if secuencia[j] == 'T':
            T = T+1
        j = j+1
        
    print "Número de nucleotidos:"
    print "Adenina:", A
    print "Citosina:", C
    print "Guanina:", T
    print "Timina:", G


def contarNucleotidos2(secuencia):
    A = C = G = T = 0
    for nucleotido in secuencia:
        if nucleotido == 'A':
            A = A+1
        if nucleotido == 'C':
            C =  C+1
        if nucleotido == 'G':
            G = G+1
        if nucleotido == 'T':
            T = T+1
    print "Número de nucleotidos:"
    print "Adenina:", A
    print "Citosina:", C
    print "Guanina:", T
    print "Timina:", G
    
DNA1 = "AGGCTGAATAGCTTTATCAGATTCGGTGTGTTTAGGCTAGCTTTCCTGATTTTGCATCAAAGCTTAATTGATAAAGCATCGGCTGCCTACCTCCTGTGCCCATAGATCTAACTTGCGGTCTTTATCTATAGGCTCTCAAGCAAGTGCCTCGCGATATGCTATTGATCAGAGGCCTCTCGAAGGGAGTTATTTTGTTTATGCCCAAACTGCACGCATCCTCGCTCCGCGCCCTCTTTAATGTGCTAGCATCCCAGTTCTCAGGCTCTATATCGCCGCCTGTCCGTTAAAAACTAGCTTTATGTTCGAGGATTTTTCGTGTGTTTAGCAGCTGGTTCGGGGGCTGGACACCATAGGCTTGAGTAGCCATATCAGTCTACCACGCTTCACGTGTTGACCTGCTTGGCCCCTTTGGTTCTTGTTATCCCGCAGGTGGGGTGTGCCGATCTACCATCGTTCGTGCGCGTTGGATTGAGGTACCATACCAAAATATTTACTAGAGCGATGTGGTACTAGAAGCTACTATAGAGCGTGTCTCAGCGTATCCGGGGACACAGTGTGATTGCTTAAAGGAATCTCTCCGCTCCTCCCCAGGAGATCCAGTTGCTAGTTCAGATCGAGAAACGGGGTCTCAACAGAGGTGAGCGGACTCGCCCGTCGAAAAGACTCTGTGTAATCATAGTGAACGAGCCCCTCAAGTTGAAAACGTTGTGAATAATACACTATGCAGCATCTCTTGGGGTCATTACGCCGATAGCGGCAGCCGGTTGCAATAATCTGGCTGACTAAATCCTACACGGAGGAGGATGTAGGGAAAGATGTCCTACGG"

print esCadenadeDNA(DNA1)
print esCadenadeDNA("ACUG")
contarNucleotidos1(DNA1)
contarNucleotidos2(DNA1)

