# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy
        t1 = l1
        t2 = l2
        carry = 0
        while t1 or t2:
            num1, num2 = 0, 0
            num1 = t1.val if t1 else 0
            num2 = t2.val if t2 else 0
            sum1 = num1 + num2 + carry

            carry = sum1 // 10
            curr.next = ListNode(sum1 % 10)
            curr = curr.next

            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next

        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next
            


        