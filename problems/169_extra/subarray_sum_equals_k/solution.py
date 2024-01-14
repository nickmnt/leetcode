class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        mem = {}
        count = 0
        for n in nums:
            s += n

            if s == k:
                count += 1
            
            if s-k in mem:
                count += mem[s-k]
            
            mem[s] = mem.get(s,0) + 1

        return count