class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        notation = 1
        
        if x < 0 :
            notation = -1
            x *= -1
        x = int(str(x)[::-1]) * notation
        
        return 0 if x < 2**31 * -1 or x > 2**31 -1 else x
    