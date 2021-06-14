def cut_ribbon():
    ribbon_len_possible = [0]*3
    len_of_ribbon, ribbon_len_possible[0], ribbon_len_possible[1], ribbon_len_possible[2] = map(int,input().split())
    
    result = [0]*10000
    result[0] = 1 
    
    for i in range(len_of_ribbon + 1):
        if result[i] != 0:
           for j in ribbon_len_possible:
               result[i+j] =  max(result[i+j], result[i]+1)
            
            
    return(result[len_of_ribbon]-1)
    
    
    
number_of_testcases = 1 #int(input())
for _ in range(number_of_testcases):
    print(cut_ribbon())