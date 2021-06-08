N = int(input())
for i in range(N + 1):
    for j in range(i, N):
        print(" ",end=" ")
    for k in range(i):
        print(k,end=" ")
            
    k = i 
    while k >= 0:
        if k == 0:
            print(k)
        else:
            print(k,end=" ")
            
        k -= 1 
    #print()
        
for i in range(N):
    for j in range(i + 1):
        print(" ", end = " ")
    if i == N-1:
        print(0)
    else:
        for j in range(N - i):
            print(j, end = " ")
        j -= 1     
        while j >= 0:
            if j == 0:
               print(j)
            else:
               print(j, end = " ")
            j -= 1 
     