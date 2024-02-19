# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # array solution

    #     myarr = []
    #     while head:
    #         myarr.append(head.val)
    #         head = head.next

    #     left, right = 0, len(myarr) - 1
    #     while left <= right:
    #         if myarr[left] != myarr[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True

    # solution 2
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # to get middle term
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse 2nd half:
        # prev will be at the last node
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check pali
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True



