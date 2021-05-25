number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    num_zeroes, num_ones, indices_possible = map(int,input().split())
    
    num_ones, num_zeroes = num_zeroes, num_ones
    
    if indices_possible%2 != 0:
        answer = (indices_possible+1)//2
        binary_string = (num_zeroes - answer)*'1' + answer*'10' + (num_ones - answer)*'0'
        
    elif num_ones>indices_possible//2:
        answer = indices_possible//2
        binary_string = (num_ones - answer)*'0' + (num_zeroes - answer)*'1' + answer*'10'
        
    else:
        answer = indices_possible//2 
        binary_string = (num_zeroes - answer)*'1' + (num_ones - answer)*'0' + answer*'01'
        
    print(binary_string)