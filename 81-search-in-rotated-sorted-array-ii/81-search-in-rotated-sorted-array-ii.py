class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = list(set(nums))
        
        if target in nums:
            return True
        return False