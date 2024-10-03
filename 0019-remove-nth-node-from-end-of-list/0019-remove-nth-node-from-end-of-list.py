# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # BF
        # if head.next is None:
        #     return None

        # count = 0
        # curr = head
        # while curr:
        #     count += 1
        #     curr = curr.next

        # m = count - n
        # if m == 0:
        #     temp = curr
        #     curr = curr.next
        #     temp.next = None
        #     return curr
      
        # curr = head
        # while curr and curr.next:
        #     m -= 1
        #     if m == 0:
        #         temp = curr.next
        #         curr.next = curr.next.next
        #         temp.next = None                
        #     curr = curr.next

        # return head

        # Optimise

        if head.next is None:
            return None

        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next

        if fast == None:
            temp = head
            head = head.next
            return head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
