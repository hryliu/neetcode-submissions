# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(pq, (l.val, i, l))

        dummy = ListNode(0)
        tail = dummy

        while pq:
            _, i, l = heapq.heappop(pq)

            tail.next = l
            tail = tail.next

            if l.next:
                heapq.heappush(pq, (l.next.val, i, l.next))

        return dummy.next


        

