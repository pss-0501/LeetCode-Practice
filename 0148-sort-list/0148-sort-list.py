# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        nums.sort()
        curr = head
        for i in range(len(nums)):
            if curr:
                curr.val = nums[i]
            curr = curr.next

        return head