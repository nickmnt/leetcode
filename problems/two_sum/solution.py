import numpy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = sorted(nums)
        indices = numpy.argsort(nums)
        l = 0
        r = len(x) - 1

        while l < r:
            cur_sum = x[l] + x[r]
            if cur_sum == target:
                return [indices[l],indices[r]]
            elif cur_sum > target:
                r -= 1
            else:
                l += 1
        return []
