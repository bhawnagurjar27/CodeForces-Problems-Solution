# Question
https://codeforces.com/problemset/problem/1520/D

Time Complexity : O(N)

# Approach
Here we can replace each ai with bi=ai−i. Then the answer is the number of pairs (i,j) such that i<j and bi=bj. 
To calculate this value we can use dictionary.