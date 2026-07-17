# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = False
        def dfs(node, total):
            nonlocal result
            if not node:
                return

            total += node.val

            if not node.left and not node.right and total == targetSum:
                result = True

            dfs(node.left, total)
            dfs(node.right, total)

        dfs(root, 0)
        return result
        