class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = str(bin(n))[2:]
        n=n[::-1]+"0"*(32-len(n))
        return int(n,2)