class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def decimalToBinary(n):
            if n == 0 :
                return 0
            return n % 2 + 10 * decimalToBinary(n // 2)
        
        def binaryToDecimal(n):
            return int(n,2)
        
        a = binaryToDecimal(a)
        b = binaryToDecimal(b)
        
        res = a + b
        res = str(decimalToBinary(res))
        return res
        