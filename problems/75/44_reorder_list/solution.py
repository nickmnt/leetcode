# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # calculate the total and the end
        total = 0
        start = head
        
        while head:
            total += 1
            prev = head
            head = head.next
        
        end = prev
        odd = total % 2 == 1
        mid = total // 2 if odd else total // 2 - 1
        
        # Reverse the pointers of the latter half
        head = start
        i = 0
        while head:
            if i > mid:
                tmp = head.next
                head.next = prev
                # print(str(head.val) + ' --> ' + str(prev.val))
                prev = head
                head = tmp
            else:
                prev = head
                head = head.next
            i += 1
        
        # Start constructing the final result
        head = start

        tail = head
        head = head.next
        for i in range(total//2):
            tail.next = end
            tail = tail.next
            end_next = end.next
            tail.next = head
            tail = tail.next
            head = head.next
            # print(str(end.val) + ' --> ' + str(end_next))
            end = end_next

        tail.next = None
