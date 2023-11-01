class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prefix = 0
        best = nums[0]
        for num in nums:
            if prefix < 0:
                prefix = 0
            prefix += num
            best = max(best, prefix)
        return best

