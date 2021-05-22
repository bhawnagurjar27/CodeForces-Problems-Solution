number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    number_of_problems, solving_skill = map(int,input().split())
    difficulty_level = list(map(int,input().split()))
    max_prob_sol = 0 
    while difficulty_level != []:
        if difficulty_level[0] <= solving_skill:
            max_prob_sol += 1 
            difficulty_level.pop(0)
        
        elif difficulty_level[-1] <= solving_skill:
            max_prob_sol += 1 
            difficulty_level.pop(-1)
            
        else:
            break
        
    print(max_prob_sol)