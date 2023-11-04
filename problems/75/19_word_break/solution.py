class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                wordlen = len(word)
                if i+wordlen <= n and s[i:i+wordlen] == word:
                    if dp[i + wordlen]:
                        dp[i] = True
                        break
        return dp[0]