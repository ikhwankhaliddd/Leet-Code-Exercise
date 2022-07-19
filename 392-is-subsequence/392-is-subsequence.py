class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        subSequence = 0
        
        for i in range(len(t)):
            if subSequence <= len(s) - 1:
                if s[subSequence] == t[i]:
                    subSequence += 1
            
        return subSequence == len(s)