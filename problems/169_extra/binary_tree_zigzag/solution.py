# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        if root:
            q.append(root)

        ltr = True
        res = []
        while q:
            lvl_items = len(q)
            vals = [x.val for x in q]
            res.append(vals if ltr else reversed(vals))
            while lvl_items:
                n = q.popleft()
                lvl_items -= 1

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            ltr = not ltr
        return res