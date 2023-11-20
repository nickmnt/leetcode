# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        best = root.val

        def dfs(n):
            nonlocal best

            if not n:
                return 0

            dfs_right = dfs(n.right)
            dfs_left = dfs(n.left)

            res = n.val + max(0, dfs_right, dfs_left)

            best = max(res, n.val+dfs_right+dfs_left, best)
            return res

        dfs(root)
        return best
        