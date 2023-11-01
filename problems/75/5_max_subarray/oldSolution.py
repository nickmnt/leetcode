class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        total = 0
        min_total = 0
        max_total = nums[0]

        for num in nums:
            total += num
            max_total = max(total - min_total, max_total)
            min_total = min(total, min_total)
        return max_total

