class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        l, r = 0, n - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # part of left portion
                l = m + 1
            else:
                # part of right portion
                r = m - 1
        return res