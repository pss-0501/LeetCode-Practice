# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.Helper(head, root):
            return True
        if not root:
            return False
        return(
            self.isSubPath(head, root.left) or
            self.isSubPath(head, root.right)
        )

    def Helper(self, llnode, treenode):
        if not llnode:
            return True
        if not treenode or llnode.val != treenode.val:
            return False
        return(
            self.Helper(llnode.next, treenode.left) or
            self.Helper(llnode.next, treenode.right)
        )
        
