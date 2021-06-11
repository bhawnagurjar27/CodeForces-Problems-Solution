t=int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        if arr[i]==1:
            x1=i 
        if arr[i]==n:
            x2=i 
            
            
    a=x1+1 
    b=x2+1 
    min1 = max(a,b)
    min2 = max(n-x1, n-x2)
    res = min(a+n-x2,b+n-x1)
    print(min(min1,min(min2,res)))
            
    