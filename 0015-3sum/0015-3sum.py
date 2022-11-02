class Solution(object):
    def twoSum(self, nums, i, result):
        nums = sorted(nums)
        n = len(nums)
        L = i + 1
        R = n -1

        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                result.append((nums[i], nums[L], nums[R]))
                L += 1
            elif nums[i] + nums[L] + nums[R] < 0:
                L += 1
            elif nums[i] + nums[L] + nums[R] > 0:
                R -= 1
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            self.twoSum(nums, i, result)
        return set(result)