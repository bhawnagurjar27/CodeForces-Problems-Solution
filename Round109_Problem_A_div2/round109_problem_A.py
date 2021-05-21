number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    number_of_contests = int(input())
    earned_points = list(map(int,input().split()))
    
    min_points = earned_points[0]
    max_points = earned_points[0] 
    num_amazing_performances = 0 
    
    for i in range(number_of_contests):
        if earned_points[i] < min_points:
            min_points = earned_points[i]
            num_amazing_performances += 1
            
        elif earned_points[i] > max_points:
            max_points = earned_points[i]
            num_amazing_performances +=1 
        
    
                
    
    print(num_amazing_performances) 