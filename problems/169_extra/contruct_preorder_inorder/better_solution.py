# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(p_start, p_end, i_start, i_end):
            nonlocal preorder, inorder

            if (p_end - p_start + 1 == 0) or (i_end - i_start + 1 == 0):
                return None
            
            root = TreeNode(preorder[p_start])

            inorder_idx = i_start
            while inorder_idx <= i_end and inorder[inorder_idx] != root.val:
                inorder_idx += 1

            root.left = build(p_start+1, p_end, i_start, inorder_idx-1)
            root.right = build(p_start+(inorder_idx - i_start)+1, p_end, inorder_idx+1, i_end)
            return root

        return build(0, len(preorder)-1, 0, len(inorder)-1)

        