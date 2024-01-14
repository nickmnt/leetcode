class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        ans = self.generateParenthesis(n-1)
        res = set()
        for a in ans:
            for i in range(len(a)):
                x = a
                x = x[:i] + '(' + x[i:]
                for j in range(i+1, len(a)+1):
                    y = x
                    y = y[:j] + ')' + y[j:]
                    res.add(y)
        return res
                