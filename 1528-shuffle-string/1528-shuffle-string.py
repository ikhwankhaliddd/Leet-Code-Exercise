class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = ""
        for i in range(len(indices)):
            if i in indices:
                ans += s[indices.index(i)]
        return ans