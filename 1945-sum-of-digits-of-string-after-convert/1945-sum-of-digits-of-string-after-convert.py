class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        al = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        for j in s:
            result += str(al.index(j) + 1) 
        for i in range(k):
            result = str(sum(int(l) for l in result))
        return result
            
            