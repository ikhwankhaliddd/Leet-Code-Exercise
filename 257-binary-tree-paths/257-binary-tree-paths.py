# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        def traversePreOrder(root,path):
            if not root.left and not root.right:
                path += str(root.val)
                ans.append(path)
                return
            if root.left:
                traversePreOrder(root.left, path + str(root.val)+ "->")
            if root.right:
                traversePreOrder(root.right, path + str(root.val) + "->")
            return
        traversePreOrder(root,"")
        return ans
        