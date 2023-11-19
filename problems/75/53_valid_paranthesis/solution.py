class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"{":"}", "[":"]","(":")"}
        for c in s:
            if c in bracket_map:
                stack.append(c)
            else:
                if len(stack) == 0 or bracket_map[stack.pop()] != c:
                    return False
        return True if len(stack) == 0 else False
            
