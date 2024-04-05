"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # Start with the root node
        queue = [root]

        while queue:
            size = len(queue)

            # Iterate through nodes at the current level
            for i in range(size):
                node = queue.pop(0)

                # Connect nodes at the same level
                if i < size - 1:
                    node.next = queue[0]

                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root