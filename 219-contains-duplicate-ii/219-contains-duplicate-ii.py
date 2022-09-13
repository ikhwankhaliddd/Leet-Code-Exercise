class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_map = {}
        
        for index,value in enumerate(nums):
            if value in hash_map and index - hash_map[value] <= k:
                return True
            hash_map[value] = index
        return False
        