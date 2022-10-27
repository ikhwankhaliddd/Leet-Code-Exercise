class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        L = 0
        R = n - 1
        m = 'aeiouAEIOU'
        
        while(L<R):
            if s[L] in m and s[R] in m:
                s[L], s[R] = s[R], s[L]
                
                L += 1
                R -= 1
            elif s[L] not in m:
                L += 1
            elif s[R] not in m:
                R -= 1
        return "".join(s)
            
        