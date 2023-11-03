https://leetcode.com/problems/coin-change  
  
O(n): The min amount of coins for each amount x is min(dp[x-coins[1]] + 1, ..., dp[x-coins[n]] + 1). We must check that x-coins[i] is >= 0. We can set 0 coins for dp[0] so that coins[i] becomes 1. Also, to check for -1 we can set amount+1 as default value for dp[i] since it is an impossible value.  
Faster solution: If statement is unnecessary after amounts larger or equal max(coins). Fix by splitting the for loop