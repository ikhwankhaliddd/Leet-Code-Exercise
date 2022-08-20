class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        if sum(map(int,str(num))) % 2 == 0:
            return num // 2
        return (num-1) // 2
        