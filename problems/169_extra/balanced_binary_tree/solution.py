# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(root, d):
            # depth fun with added problem-specific logic
            if not root:
                return d, False

            l_d, not_balanced = depth(root.left, d+1)
            # short circuit
            if not_balanced:
                return -1, not_balanced
            r_d, not_balanced = depth(root.right, d+1)
            # short circuit
            if not_balanced:
                return -1, not_balanced
            if abs(l_d - r_d) > 1:
                return max(l_d, r_d), True
            return max(l_d, r_d), False

        return not depth(root, 0)[1]