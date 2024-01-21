class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = [0,0,0]
        for n in nums:
            m[n] += 1
        j = 0
        for i in range(3):
            while m[i] > 0:
                nums[j] = i
                j += 1
                m[i] -= 1