class Node:
    def __init__(self, key, val, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.left = Node(0, 0)  # LRU
        self.right = Node(0, 0) # MRU
        # LRU - MRU
        self.left.right = self.right
        self.right.left = self.left

    def remove(self, key) -> None:
        # remove node given key
        node = self.node_map[key]
        node.right.left, node.left.right = node.left, node.right
        self.node_map.pop(key)
        return

    def insert(self, key, val) -> None:
        # insert at MRU
        node = Node(key, val)
        prev_mru = self.right.left
        self.right.left, node.right = node, self.right
        prev_mru.right, node.left = node, prev_mru
        self.node_map[key] = node
        return

    def get(self, key: int) -> int:
        if key in self.node_map:
            # remove and insert at MRU
            val = self.node_map[key].val
            self.remove(key)
            self.insert(key, val)
            return self.node_map[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.remove(key)
        # if node map is full, remove LRU
        elif len(self.node_map) == self.capacity:
            lru_key = self.left.right.key
            self.remove(lru_key)

        self.insert(key, value)
        return

        

        
