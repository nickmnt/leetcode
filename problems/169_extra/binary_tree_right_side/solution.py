# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if not root:
            return []
        q.append(root)
        res = []
        while len(q) != 0:
            level_count = len(q)
            while level_count > 0:
                n = q.popleft()
                last = n.val
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
                level_count -= 1
            res.append(last)
        return res