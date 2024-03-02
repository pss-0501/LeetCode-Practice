# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        left = head
        length = 1

        while left.next:
            left = left.next
            length += 1

        k = k % length

        left.next = head

        temp = head
        for _ in range (length - k - 1):
            temp = temp.next
        
        ans = temp.next
        temp.next = None

        return ans
