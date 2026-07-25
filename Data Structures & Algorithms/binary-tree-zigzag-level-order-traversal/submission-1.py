# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue = deque()
        queue.append(root)
        
        def traverseTree(queue):
            res = []
            level_nodes = []

            while queue:
                level_nodes = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level_nodes.append(node.val)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                res.append(level_nodes)

            return res

        res = traverseTree(queue) 

        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()

        return res  

            
        