# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        rh, lh = 0, 0

        if root.right:
            rh = self.maxDepth(root.right)

        if root.left:
            lh = self.maxDepth(root.left)

        return 1 + max(rh, lh)