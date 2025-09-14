# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.parent_map = {}

        def dfs(node):
            if not node:
                return
            if node.left:
                self.parent_map[node.left] = node
                dfs(node.left)
            if node.right:
                self.parent_map[node.right] = node
                dfs(node.right)

        dfs(root)
        visited = set()
        cur = p
        while cur:
            visited.add(cur)
            cur = self.parent_map.get(cur)
        cur = q

        while cur:
            if cur in visited:
                return cur
            cur = self.parent_map.get(cur)
