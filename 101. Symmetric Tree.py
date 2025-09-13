# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def isMirror(a:Optional[TreeNode], b:Optional[TreeNode])-> bool:
            if not a and not b:
                return True
        
            if not a or not b:
                return False
            return (a.val == b.val) and isMirror(a.left, b.right) and isMirror(a.right, b.left)

        return isMirror(root.left, root.right)
            
