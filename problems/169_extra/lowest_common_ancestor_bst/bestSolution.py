# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # r is either between both (r is parent and p,q are on both sides) then we cannot continue, best answer, anywhere we go NOT common ancestor anymore
        # r is either bigger than both (r is parent and p,q are on the left) OR
        # r is less than both (r is parent and p,q are on the right)

        r = root
        while r is not None:
            if r.val > p.val and r.val > q.val:
                r = r.left
            elif r.val < p.val and r.val < q.val:
                r = r.right
            else:
                return r
        return r