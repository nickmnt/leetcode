# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p:
                return True if not q else False
            if not q:
                return True if not p else False

            return dfs(p.left, q.left) and dfs(p.right,q.right) if p.val == q.val else False
            
        return dfs(p,q)