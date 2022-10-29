class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ["God", "Ding"]
        s = s.split(" ")
        ans = []
        for i in s:
            ans.append(i[::-1])
        return " ".join(ans)
            