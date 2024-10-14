# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        curr.next = head

        k = k % length
        end = length - k

        curr = head
        while end > 1:  # Stop at the new tail (before the new head)
            curr = curr.next
            end -= 1

        # Step 5: Break the circular connection and return the new head
        new_head = curr.next
        curr.next = None

        return new_head

