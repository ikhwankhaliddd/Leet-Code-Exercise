# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        def traverseInorder(root):
            if root is None:
                return
            traverseInorder(root.left)
            ans.append(root.val)
            traverseInorder(root.right)
            
        traverseInorder(root)
        return ans
        