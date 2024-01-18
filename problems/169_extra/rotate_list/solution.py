# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1

        if head == None:
            return None
            
        n = head
        while n.next:
            count += 1
            n = n.next
        
        k = k % count
        if k == 0:
            return head
        n.next = head
        n = head
        i = 1
        while n.next:
            if i == count-k:
                nxt = n.next
                n.next = None
                return nxt
            n = n.next
            i += 1
        return None

