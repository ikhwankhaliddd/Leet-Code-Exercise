class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def pows(n):
            if n % 4 == 0 and n > 0 :
                return pows(n//4)
            else:
                return n == 1
        return pows(n)