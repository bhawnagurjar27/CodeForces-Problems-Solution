number_of_testcases = 1 #int(input())
for _ in range(number_of_testcases):
    num_stones = int(input())
    color_of_stones = input()
    min_num_removed = 0
    for i in range(num_stones-1):
        if color_of_stones[i + 1] == color_of_stones[i]:
            min_num_removed += 1 
            
    print(min_num_removed)