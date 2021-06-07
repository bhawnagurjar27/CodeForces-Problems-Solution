def word():
    upper=0
    lower=0
    for i in range(len(given_word)):
        if ord(given_word[i])>= 97 and ord(given_word[i])<= 127:
            lower+=1 
            
        elif ord(given_word[i])>= 65 and ord(given_word[i])<= 90:
            upper+=1 
    #print(lower,upper)        
    if lower>=upper:  
        print(given_word.lower())
    else:
        
        print(given_word.upper())
        
    return given_word    
    
        
given_word = input()
word()