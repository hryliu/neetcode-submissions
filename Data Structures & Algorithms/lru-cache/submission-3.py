class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}             # key : node

        self.left = Node(0,0)       # LRU
        self.right = Node(0,0)      # MRU
        self.left.next = self.right
        self.right.prev = self.left

    # insert node at MRU end (just before self.right) 
    def insert(self, node):
        temp = self.right.prev

        self.right.prev = node
        temp.next = node

        node.next = self.right
        node.prev = temp
        
    # unlink node from list by key (does NOT touch self.cache)
    def remove(self, key):
        print(self.cache.keys())
        node = self.cache[key]
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        node = None

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove node and insert at beginning
            self.remove(key)
            node = Node(key, self.cache[key].val)
            self.insert(node)
            self.cache[key] = node
            
            return self.cache[key].val
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
            self.cache.pop(key) 

        elif len(self.cache) >= self.capacity:
            # remove LRU
            LRU_node = self.left.next
            LRU_key = LRU_node.key
            print(LRU_key)
            self.remove(LRU_key)
            self.cache.pop(LRU_key)

        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node

        
