# Question
https://codeforces.com/problemset/problem/1538/A

Time Complexity : O(N)

# Approach
In this question, We have to destroy the largest and smallest stone. so this can be done in following ways - 

1. Remove the stones on the left until we remove the smallest stone then remove the stones on the right, until we remove the largest stone.
2. Remove the stones on the right until we remove the smallest stone then remove the stones on the left, until we remove the largest stone.
3. Remove the stones on the right until we remove both stones.
4. Remove the stones on the left until we remove both stones.
Then, Here we need to check all the above four conditons and have to choose the minimum answer.