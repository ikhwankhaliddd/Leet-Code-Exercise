# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            
            return root if root.left or root.right or root.val == 1 else None