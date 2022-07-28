class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import statistics as stat
        
        arr = nums1 + nums2
        return float(stat.median(arr))