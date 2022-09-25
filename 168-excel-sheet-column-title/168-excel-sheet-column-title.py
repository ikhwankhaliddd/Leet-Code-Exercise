class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        s = ''
        
        while columnNumber > 0:
            r = columnNumber % 26
            if r == 0 :
                r = 26
            s = chr(64+r)+s
            columnNumber = int((columnNumber-r)/26)
        return s