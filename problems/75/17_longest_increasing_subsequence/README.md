https://leetcode.com/problems/longest-increasing-subsequence/  
  
O(n^2): dp[i] is at least 1 for everyone, so we initialize it to that. For each number i, traverse next numbers and if that number j is greater than them (i), then dp[j] is at least dp[i] + 1. 