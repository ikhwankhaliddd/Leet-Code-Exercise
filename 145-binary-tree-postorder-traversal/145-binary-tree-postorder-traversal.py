# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        def traversePostOrder(root):
            if root is None:
                return
            traversePostOrder(root.left)
            traversePostOrder(root.right)
            ans.append(root.val)
            
        traversePostOrder(root)
        
        return ans