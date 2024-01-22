class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        islands = 0
        
        def dfs(i, j):

            if grid[i][j] == "1":
                
                grid[i][j] = None
                
                for p,q in [(-1,0),(0,-1),(1,0),(0,1)]:
                    p += i
                    q += j

                    if p >= 0 and p < m and q >= 0 and q < n and grid[p][q] == "1":
                        dfs(p,q)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    grid[i][j] = None
                    for p,q in [(-1,0),(0,-1),(1,0),(0,1)]:
                        p += i
                        q += j

                        if p >= 0 and p < m and q >= 0 and q < n and grid[p][q] == "1":
                            dfs(p, q)
        return islands
