# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def arrToBST(arr):
            if arr == []:
                return None
            n = len(arr)
            mid = n // 2
            root = TreeNode(arr[mid])
            root.left = arrToBST(arr[:mid])
            root.right = arrToBST(arr[mid + 1:])
            
            return root
        return arrToBST(nums)