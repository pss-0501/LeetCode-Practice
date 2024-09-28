# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        nxt = curr
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        if prev:
            head = prev

        return head
