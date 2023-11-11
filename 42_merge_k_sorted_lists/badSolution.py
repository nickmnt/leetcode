# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        remaining = True
        while any(lists):
            smallest = None
            smallest_idx = -1
            for i, l in enumerate(lists):
                if l:
                    # print(l.val)
                    if smallest is None:
                        smallest = l.val
                        smallest_idx = i
                    else:
                        if l.val < smallest:
                            smallest = l.val
                            smallest_idx = i
            # print('---')
            tail.next = lists[smallest_idx]
            # print(smallest)
            # print(smallest_idx)
            # print('---')
            tail = tail.next
            lists[smallest_idx] = lists[smallest_idx].next

        return dummy.next