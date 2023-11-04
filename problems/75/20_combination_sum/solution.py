class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        n = len(candidates)

        def f(cur, i, total):
            nonlocal target, n

            res = []

            for j in range(i, n):
                c = candidates[j]
                cur.append(c)

                if total+c == target:
                    res.append(cur.copy())
                elif total+c < target:
                    res = res + f(cur.copy(), j, total+c)

                cur.pop()

            return res

        return f([], 0, 0)