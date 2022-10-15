class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        
        for i in nums:
            if nums.count(i) == 1:
                result += i
        return result