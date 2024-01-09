class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def perm(nums: List[int]):

            if len(nums) == 1:
                return [nums]

            res = []
            for l in perm(nums[1:]):
                for i in range(len(l)+1):
                    x = l.copy()
                    x.insert(i, nums[0])
                    res.append(x)
            
            return res
        
        return perm(nums)

        