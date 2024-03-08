# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_in_order():
            results = []
            def traverse(current_node):
                if current_node.left is not None:
                    traverse(current_node.left)
                results.append(current_node.val) 
                if current_node.right is not None:
                    traverse(current_node.right)          
            traverse(root)
            return results
        
        def is_valid_bst():
            nodeList = dfs_in_order()
            for i in range(len(nodeList) - 1):
                if nodeList[i] >= nodeList[i+1]:
                    return False
            return True

        tof = is_valid_bst()
        
        return tof
