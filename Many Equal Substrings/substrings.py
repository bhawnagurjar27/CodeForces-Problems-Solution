def many_equal_substrings():
    len_of_string, num_substrings = map(int,input().split())
    given_string = input()
    len1 = len_of_string
    for i in range(1,len_of_string):
        flag = 1 
        for j in range(len_of_string - i):
            if not given_string[i+j] == given_string[j]:
                flag = 0 
                break
        if flag:
            len1 = i 
            break
        
    updated_len = len_of_string - len1
    updated_str = given_string[updated_len:]
    for i in range(num_substrings-1):
        given_string += updated_str
    result = "".join(given_string)
    return result
    
number_of_testcases = 1 #int(input())
for _ in range(number_of_testcases):
    print(many_equal_substrings())