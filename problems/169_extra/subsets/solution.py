class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [[],nums]

        ans = self.subsets(nums[1:]).copy()
        res = []
        for x in ans:
            y = x.copy()
            y.append(nums[0])
            res.append(x)
            res.append(y)

        return res