class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        visited = set()
        def dfs(node) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for nb in graph[node]:
                if not dfs(nb):
                    return False

            visited.remove(node)
            graph[node] = []
            return True

        for u, _ in prerequisites:
            if not dfs(u):
                return False

        return True
