class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in x:
                return [x[diff], i] 
            x[num] = i
        return -1
