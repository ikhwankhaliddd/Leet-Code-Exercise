class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        ns = str(num)
        while len(ns) != 1:
            summ = 0
            for i in ns:
                summ += int(i)
            ns = str(summ)
        return ns
            