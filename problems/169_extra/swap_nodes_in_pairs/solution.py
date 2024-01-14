# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nxt = None
        if head and head.next:
            tmp = head.next.next
            head.next.next = head
            nxt = head.next
            head.next = self.swapPairs(tmp)
        
        return nxt if nxt else head