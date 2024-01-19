# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        res = 0

        def dfs(root, seen_sums, last_sum):
            nonlocal res

            s = last_sum + root.val
            if s == targetSum:
                res += 1
            res += seen_sums.get(s - targetSum, 0)
            
            seen_sums[s] = seen_sums.get(s,0) + 1

            if root.left:
                dfs(root.left, seen_sums, s)
            if root.right:
                dfs(root.right, seen_sums, s)

            if s in seen_sums:
                seen_sums[s] -= 1

        if root:
            dfs(root, {}, 0)

        return 0 if not root else res