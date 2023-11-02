class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        l, r = 0, n-1

        best = 0

        while l <= r:
            best = max(best, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best
            
        