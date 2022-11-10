class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        
        for res in s:
            if result and result[-1] == res:
                result.pop()
            else:
                result.append(res)
        return "".join(result)