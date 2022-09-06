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
        
        result = root.val if low <= root.val <= high else 0
#         if root.val >= high:
#             return ans  + self.rangeSumBST(root.left,low,high)
            
#         if root.val <= low:
#             return ans + self.rangeSumBST(root.right,low,high)
            
        return result + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        