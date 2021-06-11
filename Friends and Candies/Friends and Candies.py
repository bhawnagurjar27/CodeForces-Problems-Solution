number_of_testcases = int(input())

for _ in range(number_of_testcases):
    num_friends = int(input())
    candies = list(map(int,input().split()))
    sum1 = 0  
    
    for i in range(num_friends):
        sum1 += candies[i]
        
        
    if sum1 % num_friends != 0:
        print(-1)
    else:    
        sum1 = sum1/num_friends
       # print(sum1)
        min_num_selected_friends = 0
        for i in range(num_friends):
            if candies[i] > sum1:
               min_num_selected_friends += 1 
               
               
            
        print(min_num_selected_friends)
        
        
        
            
    