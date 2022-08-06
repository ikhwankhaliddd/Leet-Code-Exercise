# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root is None or self.findSymmetric(root.left,root.right)
    
    def findSymmetric(self,left,right):
        if (left is None or right is None):
            return left == right
        if (left.val != right.val):
            return False
        
        return self.findSymmetric(left.left, right.right) and self.findSymmetric(left.right, right.left)
        