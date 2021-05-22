number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    len_of_given_str, num_of_letters_to_be_removed = map(int, input().split())
    given_str = input()
    
    freq_of_alpha = [0 for i in range(26)]
    
    for char in given_str:
        freq_of_alpha[ord(char)-97] += 1 
        
    #print(freq_of_alpha)
    
    for i in range(26):
        if freq_of_alpha[i] >= num_of_letters_to_be_removed:
            freq_of_alpha[i] -= num_of_letters_to_be_removed 
            break
            
        else:
            num_of_letters_to_be_removed -= freq_of_alpha[i]
            freq_of_alpha[i] = 0 
        
    #print(freq_of_alpha)
    resulting_str = []
    
    for char in range(len_of_given_str-1, -1, -1):
        char = given_str[char]
        if freq_of_alpha[ord(char) - 97]:
            resulting_str.append(char)
            freq_of_alpha[ord(char) - 97] -= 1 
            
    #print(freq_of_alpha)
   # print(resulting_str)
    
    resulting_str.reverse()
    print("".join(resulting_str))