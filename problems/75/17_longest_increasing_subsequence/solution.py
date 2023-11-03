class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i, num in enumerate(nums):
            for j in range(i+1, n):
                if nums[j] > num:
                    dp[j] = max(dp[i] + 1, dp[j])
        return max(dp)