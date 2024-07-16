class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findPath(self, root, value, path):
        if not root:
            return False
        if root.val == value:
            return True
        path.append('L')
        if self.findPath(root.left, value, path):
            return True
        path.pop()
        path.append('R')
        if self.findPath(root.right, value, path):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        if not root or root.val == p or root.val == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def getDirections(self, root, startValue, destValue):
        startPath, destPath = [], []
        self.findPath(root, startValue, startPath)
        self.findPath(root, destValue, destPath)
        
        # Find where the paths diverge
        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1
        
        # Steps to go up from startValue to the common ancestor
        steps_up = 'U' * (len(startPath) - i)
        # Steps to go down from the common ancestor to destValue
        steps_down = ''.join(destPath[i:])
        
        return steps_up + steps_down
