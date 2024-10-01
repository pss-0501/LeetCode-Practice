# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next

        return True

            