import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # nlogn
        calc = []
        for p in points:
            # math.sqrt(p[0] ** 2 + p[1] ** 2) -> p[0] ** 2 + p[1] ** 2
            calc.append((p, p[0] ** 2 + p[1] ** 2))
        return [x[0] for x in sorted(calc, key=lambda x: x[1])[:k]]