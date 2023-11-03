class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        i_1 = 1 # ans[1]
        i_2 = 2 # ans[2]
        for i in range (3, n+1):
            ans = i_1 + i_2
            i_1 = i_2
            i_2 = ans
        return ans