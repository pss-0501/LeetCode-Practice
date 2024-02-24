# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        previous_node = dummy_node
        current_node = dummy_node.next
        
        for i in range(left - 1):
            previous_node = previous_node.next
            current_node = previous_node.next
            
        for i in range(right - left):
            node_to_move = current_node.next    #temp variable
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
    
        return dummy_node.next
        
