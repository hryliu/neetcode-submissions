# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        visited = set()

        def dfs(node):
            nonlocal res
            if node in visited: return

            visited.add(node)

            if node.val >= low and node.val <= high:
                res += node.val

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        dfs(root)

        return res