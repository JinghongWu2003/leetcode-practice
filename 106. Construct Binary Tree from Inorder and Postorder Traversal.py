# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        idx_map={val:i for i, val in enumerate(inorder)}
        self.post_index=len(postorder)-1
        def helper(left: int, right:int) ->Optional[TreeNode]:
            if left>right:
                return None
            root= TreeNode(postorder[self.post_index])
            mid=idx_map[postorder[self.post_index]]
            self.post_index-=1
            root.right=helper(mid+1,right)
            root.left=helper(left,mid-1)
            return root

        return helper(0,len(postorder)-1)