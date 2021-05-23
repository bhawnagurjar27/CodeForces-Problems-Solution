number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    size_of_matrix = int(input())
    given_matrix = []
    
    for i in range(size_of_matrix):
        row = list(map(int,input().split()))
        given_matrix.append(row)
        
    sum_of_rows = [0 for i in range(size_of_matrix)]
    sum_of_cols = [0 for i in range(size_of_matrix)]
    
    for row in range(size_of_matrix):
        for col in range(size_of_matrix):
            sum_of_rows[row] += given_matrix[row][col]
            sum_of_cols[col] += given_matrix[row][col]
    
    num_winning_squares = 0
    for row in range(size_of_matrix):
        for col in range(size_of_matrix):
            if sum_of_rows[row] < sum_of_cols[col]:
                num_winning_squares += 1 
                
    print(num_winning_squares)