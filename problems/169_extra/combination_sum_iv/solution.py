class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        mem = [0] * (target+1)
        for i in range(1, target+1):
            x = 0
            for n in nums:
                if i == n:
                    x += 1
                elif i-n >= 0:
                    x += mem[i-n]
            mem[i] = x
        return mem[target]
