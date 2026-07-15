"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        # def bfs(node) -> list:
        #     mapping = {node: Node(node.val)}
        #     queue = deque([node])

        #     while queue:
        #         curr = queue.popleft()

        #         for neighbor in curr.neighbors:
        #             if neighbor not in mapping:
        #                 mapping[neighbor] = Node(neighbor.val)
        #                 queue.append(neighbor)

        #             mapping[curr].neighbors.append(mapping[neighbor])

        #     return mapping
        
        # mapping = bfs(node)

        # return mapping[node]

        mapping = {}
        def dfs(node) -> list:
            if node in mapping:
                return mapping[node]

            clone = Node(node.val)
            mapping[node] = clone
            
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
            
        return dfs(node)

        