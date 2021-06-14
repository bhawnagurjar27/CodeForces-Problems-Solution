t=int(input())
for _ in range(t):
    n=int(input())
    
    arr = list(map(int,input().split()))
    
    x1 = dict()
    count = 0
    for i in range(n):
        z = arr[i]-i
        if(z in x1):
            count += x1[z]
            x1[z] += 1
        else:
            x1[z] = 1
    print(count)     