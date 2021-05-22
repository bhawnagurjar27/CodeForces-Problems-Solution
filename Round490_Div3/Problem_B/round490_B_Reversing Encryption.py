number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    encypted_str_len = int(input())
    encrypted_str = input()
    stored_divisors = []
    
    for i in range(encypted_str_len, 1, -1):
        if encypted_str_len % i == 0:
            stored_divisors.append(i)
            
    #print(stored_divisors)
    while len(stored_divisors) > 0:
        reverse_str = stored_divisors.pop()
        encrypted_str = encrypted_str[reverse_str-1::-1] + encrypted_str[reverse_str:] 
        
    print(encrypted_str)