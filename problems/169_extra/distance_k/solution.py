# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not target:
            return []

        p = {}
        q = deque()
        q.append(root)
        while len(q) != 0:
            n = q.popleft()
            for child in [n.left, n.right]:
                if child:
                    p[child.val] = n
                    q.append(child)
        
        q = deque()
        q.append(target)
        seen = []
        seen.append(target)
        level = 0
        while len(q) != 0:
            lvl_items = len(q)
            if level == k:
                return [n.val for n in q]
            level += 1
            while lvl_items > 0:
                n = q.popleft()
                lvl_items -= 1
                for nxt in [n.left, n.right, p.get(n.val, None)]:
                    if nxt and nxt not in seen:
                        q.append(nxt)
                        seen.append(nxt)
        return []
            