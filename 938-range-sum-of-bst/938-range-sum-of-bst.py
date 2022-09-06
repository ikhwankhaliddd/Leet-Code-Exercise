# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sum = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        self.sum = 0
        self.InorderTraversal(root,low,high)
        return self.sum
    
    def InorderTraversal(self,root,left,right):
        if not root:
            return
        
        if right < root.val:
            self.InorderTraversal(root.left,left,right)
        
        if left <= root.val <= right:
            self.InorderTraversal(root.left,left,right)
            self.sum += root.val
            self.InorderTraversal(root.right,left,right)
        if left > root.val:
            self.InorderTraversal(root.right,left,right)
        