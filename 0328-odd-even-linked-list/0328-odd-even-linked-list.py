# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # BF
        if not head:
            return None


        arr = []
        odd = head
        even = head.next

        while odd:
            k = odd.val
            arr.append(k)
            if odd.next:
                odd = odd.next.next
            else:
                break

        while even:
            k = even.val
            arr.append(k)
            if even.next:
                even = even.next.next
            else:
                break

        curr = head
        for i in arr:
            curr.val = i
            curr = curr.next

        return head