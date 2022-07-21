"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        ans = []
        
        def traversePreOrder(root):
            if root is None:
                return []
            ans.append(root.val)
            if root.children is not None:
                for i in root.children:
                    traversePreOrder(i)
        traversePreOrder(root)
        
        return ans
        