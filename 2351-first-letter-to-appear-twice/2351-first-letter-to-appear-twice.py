class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        
        for i in s:
            if i in seen:
                return i
            seen.add(i)