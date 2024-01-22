# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l, r = 0, len(nums) - 1

        def fn(l,r):
            nonlocal nums

            if l > r:
                return None

            m = (l+r)//2

            root = TreeNode(nums[m])
            root.left = fn(l,m-1)
            root.right = fn(m+1,r)

            return root
            
        return fn(0, len(nums)-1)