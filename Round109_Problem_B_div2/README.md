# Question
https://codeforces.com/contest/155/problem/B

# Approach
Initially, Sort the given number of cards according to the numbers as written at the bottom of the i-th card(bi).
         
then initialize the number of current cards to one as initially the counter is equal to one and the maximum number of points he/she can score(total score) as zero.

Step1: Under the range of cards, check whether the current number of cards is greater then one or less then one.
      
       If the current number of cards is less then one then break the loop and
         
          Decrease the counter(current number of cards) by one (As we have to discard the played card)

          increase the total score earned by he/she by the number written at the top of the card
              
          and increase the counter(current number of cards) by the number written at the bottom of the card.

Step2: Output the total score as the maximum number of points he can score in one round.

