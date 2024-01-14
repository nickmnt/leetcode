# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = True
        hd = head
        if head:
            first_even = head.next
        while hd is not None:
            nxt = hd.next.next if hd.next and hd.next.next else None
            nxt_head = hd.next
            
            if nxt:
                hd.next = nxt  
            else:
                # END
                if odd:
                    hd.next = first_even
                else:
                    hd.next = None

            hd = nxt_head     
            odd = not odd
        return head