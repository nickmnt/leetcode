# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        root = TreeNode(preorder[0])

        inorder_idx = 0
        while inorder_idx < len(inorder) and inorder[inorder_idx] != root.val:
            inorder_idx += 1

        root.left = self.buildTree(preorder[1:], inorder[:inorder_idx])
        root.right = self.buildTree(preorder[inorder_idx+1:], inorder[inorder_idx+1:])

        return root        