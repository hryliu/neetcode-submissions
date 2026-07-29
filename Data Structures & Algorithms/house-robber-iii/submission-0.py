# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> List[int]: # [with_node, without_node]
            if not root:
                return [0, 0]
            
            r_with, r_without = dfs(root.right)
            l_with, l_without = dfs(root.left)
            return [root.val + r_without + l_without, max(r_with, r_without) + max(l_with, l_without)]

        return max(dfs(root))


                