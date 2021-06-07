def word():
    upper = 0
    lower = 0
    for i in range(len(given_word)):
        if (given_word.count('7') + given_word.count('4')) == 4 or (given_word.count('7')+given_word.count('4')) == 7:
            print("YES")
            break
        else:
            print("NO")
            break
            
        
    return given_word    
    
        
given_word = input()
word()