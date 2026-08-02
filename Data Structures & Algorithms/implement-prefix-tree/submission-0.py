class TrieNode:
    def __init__(self):
        self.children = {} # char -> TrieNode
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_end_of_word = True


    def search(self, word: str) -> bool:
        node = self._find_node(word)

        if node is not None and node.is_end_of_word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return True if self._find_node(prefix) else False

    def _find_node(self, word) -> TrieNode:
        node = self.root

        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]

        return node
        
        