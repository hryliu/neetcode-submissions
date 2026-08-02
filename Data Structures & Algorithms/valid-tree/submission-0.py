class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent) -> bool:
            if node in visited:
                return False

            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False

            return True

        if dfs(0, -1) and len(visited) == n:
            return True

        return False
        
