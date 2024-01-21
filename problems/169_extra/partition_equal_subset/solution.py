class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        mem = set()
        mem.add(0)
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            new_mem = set()
            for x in mem:
                new = nums[i]+x
                new_mem.add(x)
                if nums[i] > target or new > target:
                    continue
                if new == target:
                    return True
                new_mem.add(new)
            mem = new_mem
        return False
        

        