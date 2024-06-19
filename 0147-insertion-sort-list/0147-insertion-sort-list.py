# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        sortArray = []
        while node:
            sortArray.append(node.val)
            node = node.next
        
        i = 0
        sortArray.sort()
        node = head
        while node:
            node.val = sortArray[i]
            i += 1
            node = node.next
        return head