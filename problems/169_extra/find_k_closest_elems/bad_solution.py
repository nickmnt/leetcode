class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        calc = []
        for n in arr:
            calc.append((abs(n-x)+n/10000,n))
        heapq.heapify(calc)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(calc)[1])
        return sorted(ans)
