num_testcases = 1 #int(input())
for _ in range(num_testcases):
    num_participant, time_before_break, time_after_break, percentage = map(int,input().split())
    
    result = []
    for i in range(num_participant):
        
        a, b = map(int,input().split())
        max_s = max(a*time_before_break - (percentage*a*time_before_break)/100.0 + b*time_after_break, b*time_before_break - (percentage*b*time_before_break)/100.0 + a*time_after_break)
        result.append([i+1, max_s])
    #print(result)
    
    result.sort(key = lambda c:c[1], reverse=True)
    
    for i in result:
        print(i[0],"%.2f" % i[1])