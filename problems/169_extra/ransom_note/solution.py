class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}

        for c in magazine:
            mag[c] = mag.get(c, 0) + 1
        
        for c in ransomNote:
            if c not in mag:
                return False
            if mag[c] == 0:
                return False
            mag[c] -= 1
        return True