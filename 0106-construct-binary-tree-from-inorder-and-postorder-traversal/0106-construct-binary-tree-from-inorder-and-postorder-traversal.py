# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        root_val = postorder.pop()  # Get the root node from the end of postorder
        root = TreeNode(root_val)
        mid = inorder.index(root_val)  # Find the index of root in inorder
        
        # Recursively build right subtree first
        root.right = self.buildTree(inorder[mid + 1:], postorder)
        # Then recursively build left subtree
        root.left = self.buildTree(inorder[:mid], postorder)
        
        return root
            