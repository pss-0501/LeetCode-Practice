# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        results = []
        
        def inord(node):
            if not node:
                return
            inord(node.left)
            results.append(node.val)
            inord(node.right)

        inord(root)
        tree = TreeNode(results[0])
        # to keep tree position track
        tmp = tree
        for i in results[1:]:
            tmp.right = TreeNode(i)
            tmp = tmp.right

        return tree
    
        