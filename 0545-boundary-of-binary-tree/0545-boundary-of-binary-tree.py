# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def getLeftBoundary(node):
            boundary = []
            while node:
                if not isLeaf(node):  # Ignore leaves
                    boundary.append(node.val)
                node = node.left if node.left else node.right  # Prefer left
            return boundary

        def getLeaves(node, leaves):
            if not node:
                return
            if isLeaf(node) and node != root:
                leaves.append(node.val)
            getLeaves(node.left, leaves)
            getLeaves(node.right, leaves)

        def getRightBoundary(node):
            boundary = []
            while node:
                if not isLeaf(node):
                    boundary.append(node.val)
                node = node.right if node.right else node.left
            if boundary:
                boundary.reverse()
            return boundary

        def isLeaf(node):
            return not node.left and not node.right

        leftBoundary = getLeftBoundary(root.left)
        leaves = []
        getLeaves(root, leaves)
        rightBoundary = getRightBoundary(root.right)

        return [root.val] + leftBoundary + leaves + rightBoundary