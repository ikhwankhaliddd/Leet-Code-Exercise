# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def inorder(root,arr):
            if not root:
                return
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        arr = []
        
        inorder(root,arr)
        
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True