class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k-1
        while r+1 < len(arr) and (abs(arr[r+1]-x) < abs(arr[l]-x) or arr[r+1] == arr[l]):
            l += 1
            r += 1
        return arr[l:r+1]