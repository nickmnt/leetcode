class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf') 

        val = 1
        while len(q) != 0:
            lvl_items = len(q)
            while lvl_items != 0:
                i, j = q.popleft()

                mat[i][j] = min(mat[i][j], val-1)

                for item in [(0,1),(1,0),(-1,0),(0,-1)]:
                    a, b = item
                    a += i
                    b += j

                    if a < m and b < n and a >= 0 and b >= 0 and mat[a][b] > val:
                        q.append((a, b))
                lvl_items -= 1
            val += 1
            

        return mat