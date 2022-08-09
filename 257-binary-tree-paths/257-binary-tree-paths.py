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
        def traverseDFS(root,path):
            if not root.left and not root.right:
                path += str(root.val)
                ans.append(path)
                return
            if root.left:
                traverseDFS(root.left, path + str(root.val)+ "->")
            if root.right:
                traverseDFS(root.right, path + str(root.val) + "->")
            return
        traverseDFS(root,"")
        return ans
        