class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        def calc(val, tops, bottoms):
            top = 0
            i = 0
            while i < len(tops)-1:
                i += 1
                if tops[i] == val:
                    continue
                elif bottoms[i] == val:
                    top += 1
                else:
                    break
            return top if i == len(tops)-1 else -100
        
        best = min([x for x in [calc(tops[0], tops, bottoms), 1+calc(bottoms[0], tops, bottoms), calc(bottoms[0], bottoms, tops), 1+calc(tops[0], bottoms, tops)] if x >= 0], default=-1)

        return -1 if best < 0 else best