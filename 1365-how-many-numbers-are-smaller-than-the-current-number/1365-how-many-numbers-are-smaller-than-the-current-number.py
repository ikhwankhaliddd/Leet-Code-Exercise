class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        temp = sorted(nums)
        hashMap = {}
        res = []
        for i in range(len(temp)):
            if temp[i] not in hashMap:
                hashMap[temp[i]] = i
        for i in range(len(nums)):
            res.append(hashMap[nums[i]])
        return res