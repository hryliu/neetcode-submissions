class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        visited = set()

        def dfs(node):
            if node in visited: 
                return False

            if not graph[node]:
                return True

            visited.add(node)

            neighbors = graph[node]
            for n in neighbors:
                if not dfs(n): return False

            visited.remove(node)
            graph[node] = []
            return True

        for u, _ in prerequisites:
            if not dfs(u): return False

        return True