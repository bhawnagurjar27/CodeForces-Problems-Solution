# Question
https://codeforces.com/problemset/problem/186/A

Time Complexity : O(n)

# Approach
Initally check if the length of two strings equal or not. 
     If length is not equal 
          output "NO"
     else
        We try to find the positions in strings, where chars are different. If there 1 or more than 2 such positions output "NO". 
     After that we swap 2 characters in the first string, and check for their equality.
