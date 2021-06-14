
string1 = input()
string2 = input()
#result = True
if len(string1) != len(string2):
    print("NO")
   
else:
   chars_to_be_swap = []
   for char in range(len(string1)):
        if string1[char] != string2[char]:
            chars_to_be_swap.append(char)
    
    #print(chars_to_be_swap)
if len(chars_to_be_swap) != 2:
    print("NO")
    
else:
        
    string1 = list(string1)
    string1[chars_to_be_swap[0]], string1[chars_to_be_swap[1]] = string1[chars_to_be_swap[1]], string1[chars_to_be_swap[0]]
        
    string3 = "".join(string1) 

    if string3 == string2:
       print("YES")
    else:
       print("NO")
    
    
     


   
            
    