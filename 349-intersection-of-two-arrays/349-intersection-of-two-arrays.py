class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        for i in nums1:
            if i in nums2 and nums1 and i not in ans:
                ans.append(i)
            else:
                continue
        return ans