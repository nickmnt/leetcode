class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        tot = 0
        mem = {0:0}
        best = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tot -= 1
            else:
                tot += 1
            
            if tot == 0:
                best = max(i+1, best)
            elif tot in mem:
                best = max(i - mem[tot], best)
            else:
                mem[tot] = i
        return best
            
