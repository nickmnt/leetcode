https://leetcode.com/problems/word-break/  
  
O(n.m.n): The answer until a point j starting from n-1 is True if a word in wordDict starts at j and dp[j+len(that word)] (the remainder) is True