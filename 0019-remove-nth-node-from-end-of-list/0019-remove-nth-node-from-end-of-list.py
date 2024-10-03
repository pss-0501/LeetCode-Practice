# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        m = (count - n)

        curr = head
        if m == 0 and curr == head:
            temp = curr
            curr = curr.next
            temp.next = None
            return curr

        while curr and curr.next:
            m -= 1
            if m == 0:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
                
            curr = curr.next
              

        return head