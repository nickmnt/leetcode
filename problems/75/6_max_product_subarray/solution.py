class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = max(nums)
        cur_max, cur_min = 1, 1
    
        for i, num in enumerate(nums):
            if num == 0:
                cur_max, cur_min = 1, 1
                continue

            tmp = num*cur_max
            cur_max = max(num, num*cur_max, num*cur_min)
            cur_min = min(num, tmp, num*cur_min)
            
            best = max(best, cur_max)
        
        return best
        