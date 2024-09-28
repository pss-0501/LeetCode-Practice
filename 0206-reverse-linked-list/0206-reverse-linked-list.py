# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Itterative

        # curr = head
        # prev = None
        # nxt = curr
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        # if prev:
        #     head = prev

        # return head


        # Recursive
        # Base case: if the list is empty or has only one node
        
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        reversedList = self.reverseList(head.next)
        
        # Reverse the current node by making the next node point to the current node
        head.next.next = head
        head.next = None
        
        # Return the new head of the reversed list
        return reversedList