class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for val in set(nums):
            while nums.count(val) > 2:
                nums.remove(val)
        return len(nums)