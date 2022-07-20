class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        summ = 0
        maxx = -10**4
        for i in range(len(nums)):
            summ += nums[i]
            maxx = max(summ, maxx)
            if summ < 0:
                summ = 0
        return maxx
        