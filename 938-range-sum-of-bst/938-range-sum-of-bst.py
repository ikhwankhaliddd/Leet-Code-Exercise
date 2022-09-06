# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        if not root :
            return 0
        
        RangeSumResult = root.val if low <= root.val <= high else 0
        
        if root.val >= high:
            return self.rangeSumBST(root.left,low,high) + RangeSumResult 
            
        if root.val <= low:
            return self.rangeSumBST(root.right,low,high) + RangeSumResult
            
        return self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high) + RangeSumResult
        