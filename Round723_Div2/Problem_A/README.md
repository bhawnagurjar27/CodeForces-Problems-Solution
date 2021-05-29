# Question
https://codeforces.com/contest/1526/problem/A

Time Complexity : O(NlogN)

# Approach
Firstly, Sort the numbers Then the main idea is that we can split the numbers into the two halves, the big half and small half, we can place the bigger half at the even positions and the smaller half at the odd positions.

This works because the smallest big number is larger than the biggest small number. Hence, the mean of any two big numbers is greater than any small number, and the mean of any two small numbers is smaller than any big number.
