class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        hash_map = {}
        
        for index in range(len(nums)):
            if nums[index] in hash_map and abs(index - hash_map[nums[index]]) <= k:
                return True
            hash_map[nums[index]] = index
        return False
        