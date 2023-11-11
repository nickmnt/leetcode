# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l, r = list1, list2
        if not l:
            return r
        if not r:
            return l
        if l.val > r.val or l.val == r.val:
            head = r
        else:
            head = l
        while l and r:
            if l.val > r.val or l.val == r.val:
                while r.next and (l.val > r.next.val or l.val == r.next.val):
                    r = r.next  
                tmp = r.next
                r.next = l
                r = tmp
            else:
                while l.next and r.val > l.next.val:
                    l = l.next  
                tmp = l.next
                l.next = r
                l = tmp
        return head
                
        