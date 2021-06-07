number_of_testcases = 1 #int(input())
for _ in range(number_of_testcases):
    given_string = input()
    
    given_string = list(given_string)
    if ord(given_string[0]) >= 97:
        given_string[0] = chr(ord(given_string[0]) - 32)
        
        
    answer = ""
    for char in given_string:
        answer += char
        
    print(answer)