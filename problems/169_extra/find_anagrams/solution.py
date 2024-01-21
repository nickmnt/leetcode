class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        for c in p:
            p_count[ord(c) - ord('a')] += 1
        cur_count = [0] * 26
        res = []
        for i in range(len(s)-1,-1,-1):
            cur_count[ord(s[i]) - 97] += 1
            if i+len(p) < len(s):
                cur_count[ord(s[i+len(p)]) - ord('a')] -= 1
            
            j = 0
            while j < 26:
                if p_count[j] != cur_count[j]:
                    break
                j += 1
            if j == 26:
                res.append(i)
        return res
