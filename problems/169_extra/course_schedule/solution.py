class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preq = [[] for _ in range(numCourses)]

        for crs, req in prerequisites:
            preq[crs].append(req)

        seen = set()
        def dfs(crs):
            nonlocal seen
            
            if crs in seen:
                return False
            if len(preq[crs]) == 0:
                return True

            seen.add(crs)
            for p in preq[crs]:
                if not dfs(p):
                    return False
            seen.remove(crs)

            preq[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True