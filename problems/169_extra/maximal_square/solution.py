class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        mem = [[0] * n for i in range(m)]
        for j in range(n):
            mem[m-1][j] = int(matrix[m-1][j])
        for i in range(m):
            mem[i][n-1] = int(matrix[i][n-1])
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if matrix[i][j] == "1":
                    mem[i][j] = min(mem[i+1][j], mem[i][j+1], mem[i+1][j+1])+1
        
        mx = 0
        for i in range(m):
            for j in range(n):
                mx = max(mx, mem[i][j])
        return mx**2

