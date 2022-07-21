"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        ans = []
        
        def traversePostOrder(root):
            if root is None:
                return
            if root.children is not None:
                for i in root.children:
                    traversePostOrder(i)
            ans.append(root.val)
            
        traversePostOrder(root)
        
        return ans
        