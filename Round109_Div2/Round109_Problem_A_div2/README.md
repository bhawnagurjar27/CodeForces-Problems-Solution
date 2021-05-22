# Question
https://codeforces.com/contest/155/problem/A

Time Complexity : O(N)

# Approach
Initially, initialize the min_points and max_points equal to zeroth index value of the points which the coder has earned during different contests.
Also initialize the variable "num_amazing_performances" (the number of amazing performances the coder has earned) to Zero.

Step1: Under the range of total number of contests, check whether that if minimum points/maximum points earned by the coder are greater/less then the earned points.

       If minimum points earned by the coder are greater then earned points till that index or maximum points earned by the coder less then earned points till that index
 
          then set min_points equal to that point and increase the number of amazing performances by 1.
          
          and set max_points equal to that point and increase the number of amazing performances by 1.  


Step2: Print num_amazing_performances as output.



