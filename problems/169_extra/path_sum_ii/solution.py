# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        l = []
        total = 0
        ans = []
        def dfs(r):
            nonlocal l, total, ans

            if r == None:
                return

            l.append(r.val)
            total += r.val
            if total == targetSum and not r.left and not r.right:
                ans.append(l.copy())
            dfs(r.left)
            dfs(r.right)
            l.pop()
            total -= r.val

        dfs(root)
        return ans