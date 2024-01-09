# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        best = None, -1

        def traverse(r, depth):
            nonlocal p,q, best

            if not r:
                return False, False

            p_seen, q_seen = r.val == p.val, r.val == q.val

            if (p.val < r.val and not p_seen) or (q.val < r.val and not q_seen):
                p_seen_next, q_seen_next = traverse(r.left, depth)
                p_seen |= p_seen_next
                q_seen |= q_seen_next

            if (p.val > r.val and not p_seen) or (q.val > r.val and not q_seen):
                p_seen_next, q_seen_next = traverse(r.right, depth)
                p_seen |= p_seen_next
                q_seen |= q_seen_next

            best_val, best_d = best
            if depth > best_d and p_seen and q_seen:
                best = (r, depth)

            return p_seen, q_seen

        traverse(root, 0)
        return best[0]
        