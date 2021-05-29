number_of_testcases = 1 #int(input())
for _ in range(number_of_testcases):
    number_of_points = int(input())
    coordinates = [list(map(int,input().split())) for i in range(number_of_points)]
    #print(coordinates)
    num_supercentral_points = 0 
    
    for i in coordinates:
        correct_set = 0
        for j in coordinates:
            if i[0]>j[0] and i[1]==j[1]:
                correct_set += 1 
                break
        for j in coordinates:
            if i[0]<j[0] and i[1]==j[1]:
                correct_set += 1 
                break
        for j in coordinates:
            if i[0]==j[0] and i[1]>j[1]:
                correct_set += 1 
                break
        for j in coordinates:
            if i[0]==j[0] and i[1]<j[1]:
                correct_set += 1 
                break
        
        if correct_set == 4:
            num_supercentral_points += 1
            
    print(num_supercentral_points)