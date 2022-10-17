class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = set(range(1,len(nums)+1)) - set(nums)
        return ans
        