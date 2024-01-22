class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preq = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            preq[dst].append(src)
        
        seen = set()
        all_seen = set()
        res = []
        def dfs(crs):
            nonlocal seen, res, all_seen

            if crs in seen:
                return False
            if preq[crs] == []:
                if crs not in all_seen:
                    all_seen.add(crs)
                    res.append(crs)
                return True

            seen.add(crs)
            for c in preq[crs]:
                if not dfs(c):
                    return False
            seen.remove(crs)

            if crs not in all_seen:
                preq[crs] = []
                all_seen.add(crs)
                res.append(crs)

            return True
        
        for c in range(numCourses):
            if c not in all_seen and not dfs(c):
                return []

        return res

