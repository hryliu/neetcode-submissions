class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build graph and do post order dfs

        graph = {c: set() for word in words for c in word}  # every character is a node, even isolated ones

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ''

            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        visited = {} # True - visited and in current res
                     # False - visited

        res = []

        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node] = False

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = True
            res.append(node)
            return True

        for l in graph:
            if not dfs(l):
                return ''

        res.reverse()
        return ''.join(res)
            
