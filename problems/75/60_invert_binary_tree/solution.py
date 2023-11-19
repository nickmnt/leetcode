# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(n):
            if not n:
                return

            dfs(n.left)
            dfs(n.right)
            tmp = n.left
            n.left = n.right
            n.right = tmp
        
        dfs(root)
        return root