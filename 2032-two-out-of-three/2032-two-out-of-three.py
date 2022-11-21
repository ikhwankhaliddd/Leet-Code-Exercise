class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        temp = list(set())
        
        res = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        
        finalAns = list(set())
        
        for number in res:
            if number in temp:
                finalAns.append(number)
            temp.append(number)
        return list(set(finalAns))