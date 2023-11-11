class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        res = 0
        for num in nums:
            tmp = res
            res = max(res, prev+num)
            prev = tmp
        return res