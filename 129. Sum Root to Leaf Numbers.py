# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dps(root: Optional[TreeNode], sum):
            if not root:
                return 0
            sum *= 10
            sum += root.val
            if not root.left and not root.right:
                return sum
            return dps(root.left, sum) + dps(root.right, sum)

        return dps(root, 0)



