# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # BF

        # myDict = {}
        # curr1 = headA
        
        # while curr1:
        #     myDict[curr1] = 1
        #     curr1 = curr1.next

        # curr2 = headB
        # while curr2:
        #     if curr2 in myDict:
        #         return curr2
        #     curr2 = curr2.next

        # return None

        # Optimise

        curr1 = headA
        lenA = 0
        while curr1:
            lenA += 1
            curr1 = curr1.next

        curr2 = headB
        lenB = 0
        while curr2:
            lenB += 1
            curr2 = curr2.next

        if lenA < lenB:
            tA = headA
            tB = headB
            d = lenB - lenA
            while d > 0:
                tB = tB.next
                d -= 1
        else:
            tB = headB
            tA = headA
            d = lenA - lenB
            while d > 0:
                tA = tA.next
                d -= 1

        while tA and tB:
            if tA == tB:
                return tA
            
            tA = tA.next
            tB = tB.next

        return None
