# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        dummy = ListNode()
        dummy.next = head
        def find_node(idx) -> Tuple[ListNode, ListNode]:
            temp = head
            prev = dummy
            curr_idx = 1
            while temp:
                if curr_idx == idx:
                    return prev, temp
                prev = temp
                temp = temp.next
                curr_idx += 1

        l_prev, l_node = find_node(left)
        _, r_node = find_node(right)
        r_next = r_node.next

        prev = None
        node = l_node
        idx = 0
        while idx < right - left + 1:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            idx += 1

        l_prev.next = prev
        l_node.next = r_next

        return dummy.next
        

        