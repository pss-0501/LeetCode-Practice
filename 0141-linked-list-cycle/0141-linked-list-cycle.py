# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute Force
        visited = set()
        curr = head
        while curr:
            if curr in visited:  # Checking if we've seen this node before
                return True
            visited.add(curr)  # Add current node to visited set
            curr = curr.next  # Move to the next node
        return False