def problemA():
    N, M = map(int,input().split())
    prime_numbers = []
    for prime in range(N, M+1):
        if prime > 1:
            for i in range(2, prime):
                if prime % i == 0:
                    break
            else:
                prime_numbers.append(prime)
    #print(prime_numbers)
    if len(prime_numbers) > 1:
        if prime_numbers[1] == M:
            return "YES"
            
        else:
            return "NO"
    else:
        return "NO"
                
    

number_of_testcases = 1 #int(input())
for _ in range(number_of_testcases):
    print(problemA())