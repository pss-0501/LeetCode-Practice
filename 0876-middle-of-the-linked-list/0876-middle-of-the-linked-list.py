# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # BF
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        mid = (count // 2) + 1
        curr = head
        while curr:
            mid = mid -1
            if mid == 0:
                break
            curr = curr.next
        return curr
        

        # Optimise
        # fast = head
        # slow = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow

        


        