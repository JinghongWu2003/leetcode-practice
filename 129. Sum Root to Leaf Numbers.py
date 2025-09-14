# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        array = []

        def dps(root: Optional[TreeNode], sum):
            if not root:
                return
            sum *= 10
            sum += root.val
            if not root.left and not root.right:
                array.append(sum)

            if root.left:
                dps(root.left, sum)
            if root.right:
                dps(root.right, sum)

        dps(root.right, root.val)
        dps(root.left, root.val)

        if not root.left and not root.right:
            return root.val

        return sum(array)



