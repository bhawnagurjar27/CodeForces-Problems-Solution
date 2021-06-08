number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    num_elements = int(input())
    array_elements = list(map(int, input().split()))
    
    num_queries = int(input())
    search_queries = list(map(int, input().split()))
    
    index_value1 = {}
    index_value2 = {}
    
    for i in range(len(array_elements)):
        index_value1[array_elements[i]] = [i+1]
        index_value2[array_elements[i]] = [num_elements - i]
        
    count_from_starting = 0
    count_from_end = 0 
    
    for i in range(num_queries):
        count_from_starting += index_value1[search_queries[i]][0]
        count_from_end += index_value2[search_queries[i]][0]
        
        
    print(count_from_starting, count_from_end)
        