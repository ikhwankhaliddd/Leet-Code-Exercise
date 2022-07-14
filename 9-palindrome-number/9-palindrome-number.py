class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        InttoString = str(x)
        
        if (InttoString == InttoString[::-1] ):
            InttoString = int(InttoString)
            return True
        return False