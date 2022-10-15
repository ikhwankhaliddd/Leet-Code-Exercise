class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        sortedTarget = sorted(target)
        sortedArr = sorted(arr)
        if sortedTarget != sortedArr:
            return False
        return True