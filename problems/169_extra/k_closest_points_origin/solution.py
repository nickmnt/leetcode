import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # nlogn
        calc = []
        for p in points:
            calc.append((p, math.sqrt(p[0] ** 2 + p[1] ** 2)))
        return [x[0] for x in sorted(calc, key=lambda x: x[1])[:k]]