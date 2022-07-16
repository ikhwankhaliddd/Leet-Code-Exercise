class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sums = sum(nums)
        temp = (len(nums) * (len(nums) + 1)) // 2
        return temp - sums