class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh_count = 0
        # BFS
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        if fresh_count == 0:
            return 0
        
        level_items = len(q)
        levels = 0
        while len(q) != 0:
            i, j = q.popleft()
            level_items -= 1
            level_end = False
            if level_items == 0:
                level_end = True

            for a, b in [(0,1),(1,0),(-1,0),(0,-1)]:
                a = i+a
                b = j+b

                if (a >= 0 and a < m) and (b >= 0 and b < n):
                    if grid[a][b] == 1:
                        grid[a][b] = 2
                        q.append((a,b))

            if level_end:
                level_items = len(q)
                # print(q)
                if level_items != 0:
                    levels += 1
        
        fresh_count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
        if fresh_count != 0:
            return -1

        return levels
