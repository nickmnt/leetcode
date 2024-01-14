class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        orig = 0
        i = 0
        val = nums[0]

        items = 0
        while items < len(nums):
            next_i = (i+k) % len(nums)
            tmp = nums[next_i]
            nums[next_i] = val
            if next_i == orig and orig != len(nums)-1:
                orig = orig+1
                val = nums[orig]
                i = orig
            else:
                val = tmp
                i = next_i
            items += 1  

        return nums