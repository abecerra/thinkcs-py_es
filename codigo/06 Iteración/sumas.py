
#mal, falta el valor k
def suma1(k):
    j = 1
    while k!=j:
        print(j)
        j = j+1

#bien
def suma2(k):
    s = 0
    j = 1
    while j!=k+1:
        s = s+j
        j = j+1
    return s
#suma1(8)

#bien
def suma3(k):
    j = 1
    s = 0
    while j<=k:
        s = s+j
        j = j+1
    return s
#bien
def suma4(k):
    s = 0
    j = k
    while j!=0 :
        s = s+j
        j = j-1
    return s

#bien
def suma5(k):
    s = 0
    j = k
    while j>0 :
        s = s+j
        j = j-1
    return s

def factorial(k):
    s = 1
    j = k
    while j>0 :
        s = s*j
        j = j-1
    return s        

#print suma2(1)
#print suma3(2)
#print suma4(3)
#print suma5(4)
for j in range(1,10):
    print(j,":\t",factorial(j))
    
for j in range(1,10):
    print(j,":\t",factorial(j))

