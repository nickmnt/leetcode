import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # klogn
        calc = []
        for p in points:
            calc.append((p[0] ** 2 + p[1] ** 2, p))
        # n
        heapq.heapify(calc)
        res = []
        # klogn
        for i in range(k):
            # logn
            res.append(heapq.heappop(calc)[1])
        return res