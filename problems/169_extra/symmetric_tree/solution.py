# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return True

        def fn(l, r):
            
            if (l and not r) or (r and not l):
                return False

            if (not l and not r):
                return True

            if l.val != r.val:
                return False

            return fn(r.left, l.right) and fn(r.right, l.left)

        return fn(root.left, root.right)