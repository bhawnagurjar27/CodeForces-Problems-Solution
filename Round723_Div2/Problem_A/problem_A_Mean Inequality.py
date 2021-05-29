number_of_testcases = int(input())
 
for _ in range(number_of_testcases):
   N = int(input())
   given_array = list(map(int, input().split()))
   
   given_array.sort(reverse=True)
   first_half = given_array[:N]
   second_half = given_array[N:]
   
   for i, v in enumerate(second_half):
        first_half.insert(2*i+1, v)
               
   print(*first_half)
           