# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            print(node.val, ': ', left, right)

            # take path with max sum

            if left < 0 and right < 0:
                max_sum = max(max_sum, node.val)
                return node.val

            _sum = node.val + left + right
            if left < 0:
                _sum += abs(left)

            if right < 0:
                _sum += abs(right)

            print(_sum)

            max_sum = max(max_sum, _sum)
            return max(node.val + left, node.val + right)

        dfs(root)
        return max_sum

