# Question
https://codeforces.com/problemset/problem/139/A

Time Complexity : O(N)

# Approach
In this problem, If the total number of pages doesn't exceed the number of pages for Monday, the answer is Monday. Otherwise we can substract the Monday number from total and go on to Tuesday. If Tuesday is not possible, we subtract and continue to Wednesday, and so on. 
We are sure that no more than N weeks will pass, as at least one page is read every week.