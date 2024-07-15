# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parents, child, left in descriptions:
            if parents not in nodes:
                nodes[parents] = TreeNode(parents)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            children.add(child)

            if left:
                nodes[parents].left = nodes[child]
            else:
                nodes[parents].right = nodes[child]
            
        root = None
        for node in nodes:
            if node not in children:
                root = nodes[node]
                break
        
        return root