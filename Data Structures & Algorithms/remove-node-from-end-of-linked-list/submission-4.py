# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        idx = 0
        list_len = 0

        while(curr):
            list_len += 1
            curr = curr.next

        position = list_len - n

        curr = head
        if position == 0:
            head = curr.next
            curr = None
            return head

        while(curr and idx < position):
            prev = curr
            curr = curr.next
            idx += 1

        prev.next = curr.next
        curr = None
        return head