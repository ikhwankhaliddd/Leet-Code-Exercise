# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        ans = {i:self.res.count(i) for i in self.res}
        
        max_val = max(ans.values())
        
        return [i for i,j in ans.items() if j == max_val]
            