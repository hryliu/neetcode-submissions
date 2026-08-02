class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word) and node and node.is_end_of_word:
                return True

            if i < len(word) and word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i + 1): return True

            else:
                if i < len(word) and word[i] in node.children:
                    if dfs(node.children[word[i]], i + 1): return True
            
            return False

        return dfs(self.root, 0)

            


        
