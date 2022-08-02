# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recursive(root):
    if not root:
        return float('inf')
    if not root.left and not root.right:
        return 1
    return min(1+ recursive(root.left), 1 + recursive(root.right))

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return recursive(root)
        