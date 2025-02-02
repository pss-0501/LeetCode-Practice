# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_items = defaultdict(list)
        queue = deque()
        queue.append((root, 0, 0))

        while queue:
            node, row, col = queue.popleft()
            
            level_items[col].append((row, node.val))

            if node.left:
                queue.append((node.left, row + 1, col - 1))

            if node.right:
                queue.append((node.right, row + 1, col + 1))

        result = []
        for x in sorted(level_items.keys()):
            column = sorted(level_items[x])  # Sort by y (first), then by value
            result.append([val for y, val in column])

        return result