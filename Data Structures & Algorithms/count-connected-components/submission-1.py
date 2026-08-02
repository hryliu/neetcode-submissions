class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        connected_comp = 0
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

            
        for node in range(n):
            if node not in visited:
                connected_comp += 1
                dfs(node)

        return connected_comp