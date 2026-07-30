class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        # cat -> bat
        # bat -> bag
        # bag -> sag

        # build adjacency list of root words -> words it can become

        # b*t: [bat]
        # ba*: [bat, bag]

        # start at begin word, init layer to 1
        # multi source bfs search - track visited - to see if i can arrive at end word

        adj_words = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                root_word = word[:i] + '*' + word[i+1:]
                adj_words[root_word].append(word)

        queue = deque()
        visited = set()

        for i in range(len(beginWord)):
            root_word = beginWord[:i] + '*' + beginWord[i+1:]
            visited.add(root_word)
            queue.append((root_word, 1))

        while queue:
            for _ in range(len(queue)):
                word, layer = queue.popleft()

                if word in adj_words:
                    for adj_word in adj_words[word]:
                        if adj_word == endWord:
                            return layer + 1

                        for i in range(len(adj_word)):
                            next_word = adj_word[:i] + '*' + adj_word[i+1:]
                            if next_word not in visited:
                                visited.add(next_word)
                                queue.append((next_word, layer + 1))

        return 0

                        