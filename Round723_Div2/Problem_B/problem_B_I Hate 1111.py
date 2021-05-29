number_of_testcases = int(input())
for _ in range(number_of_testcases):
    number = int(input())
    
    while number != 0:
        if number % 11 == 0:
            print("YES")
            break
        if number % 111 == 0:
            print("YES")
            break
        if number < 111:
            print("NO")
            break
        
        number -= 111
    