class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,2,2,3,3] -> return 1
        # 1. traverse into entire array
        # 2. check whether the element in array just one or not
        # 2a. if one : return its element
        # 2b. else: continue
        
        for i in nums:
            if nums.count(i) == 1:
                return i
            continue
        return nums[0]