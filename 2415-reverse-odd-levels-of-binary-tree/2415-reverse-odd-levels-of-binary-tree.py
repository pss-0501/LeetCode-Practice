# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use deque for BFS, which allows efficient appends and pops from both ends
        queue = deque([root])
        level = 0  # Start from the root level, which is level 0 (even)

        # List to hold all nodes at the current level
        level_nodes = []
        while queue:
            # Number of nodes at the current level
            level_size = len(queue)
            current_level = []

            # Process each node at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)

                # Enqueue child nodes if they exist
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)

            # Reverse the values at odd levels
            if level % 2 == 1:
                # Collect values and reverse them without using zip
                values = [node.val for node in current_level]
                reversed_values = list(reversed(values))
                
                # Manually assign reversed values to nodes
                for i in range(len(current_level)):
                    current_level[i].val = reversed_values[i]

            # Increment level count after processing each level
            level += 1

        return root        