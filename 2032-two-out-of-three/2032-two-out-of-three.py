class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        finalAns = []
        counter = 0
        for i in nums3:
            if i in nums2 or i in nums1:
                finalAns.append(i)
        for j in nums2:
            if j in nums3 or j in nums1:
                finalAns.append(j)
        for l in nums1:
            if l in nums2 or l in nums3:
                finalAns.append(l)
        return list(set(finalAns))