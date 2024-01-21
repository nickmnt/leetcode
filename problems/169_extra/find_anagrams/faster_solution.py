class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        for c in p:
            # 97 = ord('a')
            p_count[ord(c) - 97] += 1
        res = []
        for i in range(len(s)-1,-1,-1):
            p_count[ord(s[i]) - 97] -= 1
            if i+len(p) < len(s):
                p_count[ord(s[i+len(p)]) - 97] += 1
            
            j = 0
            while j < 26:
                if p_count[j] != 0:
                    break
                j += 1
            if j == 26:
                res.append(i)
        return res
