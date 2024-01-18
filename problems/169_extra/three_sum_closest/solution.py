class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        best_diff = float('inf')
        best = None
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            a = nums[i]

            l, r = i+1, len(nums)-1
            while l < r:
                s = a + nums[l] + nums[r]
                diff = s - target
                abs_diff = abs(diff)

                if abs_diff < best_diff:
                    best_diff = abs_diff
                    best = s

                if diff < 0:
                    l += 1
                elif diff > 0:
                    r -= 1
                else:
                    return target
        return best