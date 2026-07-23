# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def level_order(root):
            if not root:
                return []

            queue = deque([root])
            res = []

            while queue:
                level_size = len(queue)
                level = []

                for _ in range(level_size):
                    node = queue.popleft()

                    if node:
                        level.append(str(node.val))
                    else:
                        level.append('')
                        continue

                    queue.append(node.left)
                    queue.append(node.right)

                res.append(level)

            return res

        levels = level_order(root)
        print(levels)

        res = ''
        for l in levels:
            for s in l:
                res = res + s + ','

        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(',')
        print(values)

        if not values or values[0] == '':
            return None

        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1
        while(queue and i < len(values)):
            node = queue.popleft()

            # build left
            if i < len(values):
                if values[i] != '':
                    left = TreeNode(int(values[i]))
                    node.left = left
                    queue.append(left)
                i += 1

            # build right
            if i < len(values):
                if values[i] != '':
                    right = TreeNode(int(values[i]))
                    node.right = right
                    queue.append(right)
                i += 1

        return root
