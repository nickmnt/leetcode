class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        chars = set()
        for c in s:
            a[c] = 1 + a.get(c, 0)
            chars.add(c)
        for c in t:
            b[c] = 1 + b.get(c, 0)
            chars.add(c)
        for c in chars:
            if a.get(c, 0) != b.get(c, 0):
                return False
        return True 