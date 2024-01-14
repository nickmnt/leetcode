# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,0))
        best = 1
        while len(q) != 0:
            lvl_items = len(q)
            first_node = q[0][1]
            last_node = q[-1][1]
            while lvl_items != 0:
                n, n_i = q.popleft()
                lvl_items -= 1
                if n:
                    if n.left:
                        q.append((n.left,n_i*2))
                    if n.right:
                        q.append((n.right,n_i*2+1))
                    
            best = max(last_node - first_node + 1, best)
        return best