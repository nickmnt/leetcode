# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        l = []
        def inorder(n):
            nonlocal l

            if not n:
                return

            inorder(n.left)
            l.append(n.val)
            inorder(n.right)
        
        inorder(root)
        return l[k-1]