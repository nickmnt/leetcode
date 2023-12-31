# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        best = -1
        while l <= r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m-1
                best = m
            else:
                l = m+1
        return best