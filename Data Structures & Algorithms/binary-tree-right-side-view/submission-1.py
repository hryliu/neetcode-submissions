# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        def level_order(root: Optional[TreeNode]) -> List[List[int]]:
            levels = []

            queue = deque([root])

            while(queue):
                level_len = len(queue)
                level_vals = []

                for _ in range(level_len):
                    curr = queue.popleft()
                    level_vals.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)

                    if curr.right:
                        queue.append(curr.right)

                levels.append(level_vals)

            return levels

        levels = level_order(root)
        right_side_view = []

        for l in levels:
            right_side_view.append(l[-1])

        return right_side_view
            