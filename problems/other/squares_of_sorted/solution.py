class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1

        neg = nums[:i]
        pos = nums[i:]

        neg = list(reversed([x**2 for x in neg]))
        pos = [x**2 for x in pos]
        
        res = []
        i = 0
        a = 0
        b = 0
        while True:
            if a < len(neg) and b < len(pos):
                if neg[a] <= pos[b]:
                    res.append(neg[a])
                    a += 1
                else:
                    res.append(pos[b])
                    b += 1
            elif a < len(neg):
                res = res + neg[a:]
                break
            elif b < len(pos):
                res = res + pos[b:]
                break
        return res