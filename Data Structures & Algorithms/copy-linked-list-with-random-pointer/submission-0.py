"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        copied_nodes = {None: None} # old: new

        while(curr):
            copy = Node(curr.val)
            copied_nodes[curr] = copy
            curr = curr.next

        curr = head
        while(curr):
            copy = copied_nodes[curr]
            copy.next = copied_nodes[curr.next]
            copy.random = copied_nodes[curr.random]
            curr = curr.next

        return copied_nodes[head]


        

            