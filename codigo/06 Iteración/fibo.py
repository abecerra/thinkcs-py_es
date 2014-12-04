

# k : 0 1 2 3 4 5 ...
# f : 0 1 1 2 3 5 ...
#    -----^

##def fibonacci():
##
##    fn_1 = 1 
##    fn_2 = 0
##    k = 2
##
##    while k <= 10:
##        #print k
##        fn = fn_2 + fn_1
##        print fn
##        fn_2 = fn_1
##        fn_1 = fn
##        
##        
##        k = k +1
##        
##
##fibonacci()
        

def fibonacci(n):

    if n == 0:
        return 0
    elif n== 1:
        return 1

    fn_1 = 1 
    fn_2 = 0
    k = 2


    while k <= n:
        fn = fn_2 + fn_1
        fn_2 = fn_1
        fn_1 = fn
        k = k +1

    return fn
        


j = 0
while j <= 15:
    print(j, "  ",fibonacci(j))
    j = j+1
    
