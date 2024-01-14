class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(l, op, cl):
            nonlocal n,res
            if op == cl == n:
                res.append(''.join(l))
            
            if cl < op:
                l.append(')')
                backtrack(l, op, cl+1)
                l.pop()

            if op < n:
                l.append('(')
                backtrack(l, op+1,cl)
                l.pop()

        backtrack([], 0, 0)
        return res


                