class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        hash_map = {}
        
        for index,value in enumerate(nums):
            if value in hash_map and index - hash_map[value] <= k:
                return True
            hash_map[value] = index
        return False
        