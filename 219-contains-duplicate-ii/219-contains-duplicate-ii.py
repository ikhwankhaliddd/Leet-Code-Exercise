class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_map = {}
        
        for index,value in enumerate(nums):
            if value in hash_map and abs(hash_map.get(value) - index) <= k:
                return True
            else:
                hash_map[value] = index
        return False
        