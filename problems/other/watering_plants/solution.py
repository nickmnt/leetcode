class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        w = capacity
        ans = 0
        for i, c in enumerate(plants):
            if w >= c:
                w -= c
                ans += 1
            else:
                ans += i + i + 1
                w = capacity - c
        return ans