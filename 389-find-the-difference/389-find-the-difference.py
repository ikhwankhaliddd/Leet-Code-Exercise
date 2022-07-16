class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        str1 = list(s)
        str2 = list(t)
        str1.sort()
        str2.sort()
        for i in range(len(str1)):
            if str2[i] != str1[i]:
                return str2[i]
        return str2[-1]
        