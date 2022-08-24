# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return

        queue = []
        ans = []
        queue.append(root)

        while(len(queue) > 0):
            res = []
            length = len(queue)
            for length in range(length):
                node = queue.pop(0)
                res.append(node.val)
                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)
            ans.append(res)
        return ans
        