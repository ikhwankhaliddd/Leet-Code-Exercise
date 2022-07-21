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
        
        def traverseInOrder(root):
            if root is None:
                return
            traverseInOrder(root.left)
            ans.append(root.val)
            traverseInOrder(root.right)
            
        traverseInOrder(root)
        
        return ans
        