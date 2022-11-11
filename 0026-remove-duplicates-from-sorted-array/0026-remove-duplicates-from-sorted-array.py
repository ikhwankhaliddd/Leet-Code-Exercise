class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(1, n):
            if nums[ans] != nums[i]:
                ans += 1
                nums[ans] = nums[i]
        return ans + 1
        