class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        mx_coin = max(coins)
        for i in range(1, min(mx_coin, amount+1)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        for i in range(mx_coin, amount+1):
            for coin in coins:
                dp[i] = min(dp[i - coin] + 1, dp[i])
        
        return dp[amount] if dp[amount] != amount + 1 else -1