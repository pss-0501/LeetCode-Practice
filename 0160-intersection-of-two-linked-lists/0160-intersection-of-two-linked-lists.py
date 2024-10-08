# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        myDict = {}
        curr1 = headA
        
        while curr1:
            myDict[curr1] = 1
            curr1 = curr1.next

        curr2 = headB
        while curr2:
            if curr2 in myDict:
                return curr2
            curr2 = curr2.next

        return None
