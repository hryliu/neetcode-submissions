class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        visited = set()
        result = []

        def dfs(node):
            if node in visited:
                return False
            if not graph[node]:
                if node not in result:
                    result.append(node)
                return True

            visited.add(node)

            for n in graph[node]:
                if not dfs(n):
                    return False

            visited.remove(node)
            graph[node] = []
            if node not in result:
                result.append(node)
            return True

        for u, v in prerequisites:
            graph[u].append(v)

        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return result
                

