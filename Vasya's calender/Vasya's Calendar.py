def vasyas_Calendar():
    max_num_of_days = int(input())
    num_months_in_year = int(input())
    num_days_each_month = list(map(int,input().split()))
    
    answer = 0
    for i in range(num_months_in_year - 1):
        answer += (max_num_of_days - num_days_each_month[i])
        
    return answer
    



number_of_testcases = 1 #int(input())
for _ in range(number_of_testcases):
    print(vasyas_Calendar())