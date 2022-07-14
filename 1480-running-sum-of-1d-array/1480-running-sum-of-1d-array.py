class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [nums[0]]
        
        for i in range(1,n):
            nums[i] += nums[i-1]
            result.append(nums[i])
        return result