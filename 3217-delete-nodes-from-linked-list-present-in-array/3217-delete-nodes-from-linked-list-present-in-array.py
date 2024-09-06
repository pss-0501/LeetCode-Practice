# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(0)  # Dummy node to handle edge cases
        dummy.next = head
        prev, curr = dummy, head
        
        while curr:
            if curr.val in nums_set:
                # Skip the current node by updating the next pointer of the previous node
                prev.next = curr.next
            else:
                # Move the prev pointer to the current node if it shouldn't be deleted
                prev = curr
            curr = curr.next
        
        return dummy.next