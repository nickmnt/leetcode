class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = set()
        for i, num_i in enumerate(nums):
            x = {}

            for j, num_j in enumerate(nums):
                if j == i:
                    continue
                diff = 0 - num_i - num_j
                if diff in x:
                    results.add((num_i,num_j,diff))

                x[num_j] = j  
        return list(results)