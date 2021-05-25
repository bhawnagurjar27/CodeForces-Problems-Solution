number_of_testcases = 1 #int(input())
for _ in range(number_of_testcases):
    number_of_coins = int(input())
    value_of_coins = list(map(int,input().split()))
    min_pockets = 0 
    values = dict()
    for i in value_of_coins:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1 
    
    for i in values:        
        min_pockets = max(min_pockets, values[i])
     
    print(min_pockets)
        