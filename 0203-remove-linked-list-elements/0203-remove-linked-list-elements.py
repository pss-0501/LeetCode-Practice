# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        prev.next = head
        cur = head
        while cur:
                
            if cur.val == val:
                prev.next = cur.next
                #cur.next = None
            else:
                prev = cur
            cur = cur.next

        return dummy.next   # to not return 0th node which we gave to prev in start
