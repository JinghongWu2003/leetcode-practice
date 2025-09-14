# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.flag=False
        def dfs(root: Optional[TreeNode], target: int) -> bool:
            if not root:
                return False
            if not root.left and not root.right:
                if root.val==target:
                    self.flag=True
            if root.left:
                root.left.val+=root.val
                dfs(root.left,target)
            if root.right:
                root.right.val+=root.val
                dfs(root.right,target)
        dfs(root, targetSum)
        return self.flag