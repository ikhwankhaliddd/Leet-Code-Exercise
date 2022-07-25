class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        for i in range(len(nums)):
            if nums[i] == target:
                 lst.append(i)
            
        if (len(lst) == 0) :
            return [-1,-1]
        else:
            res = []
            res.append(min(lst))
            res.append(max(lst))
            return res
        