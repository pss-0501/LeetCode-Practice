# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        ttl = 0

        def DFS(node, curPath):
            if not node:
                return
            newPath = curPath + [node.val]

            # Check if current node is a leaf and if the path sum matches targetSum
            if node.left is None and node.right is None:
                if sum(newPath) == targetSum:
                    res.append(newPath)
                return

            # Recursive calls to left and right children with updated path
            DFS(node.left, newPath)
            DFS(node.right, newPath)

        DFS(root, [])  # Initialized as an empty list, not 0
        return res