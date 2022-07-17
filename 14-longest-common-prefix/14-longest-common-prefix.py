class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]
        
        i = 1
        
        while i < len(strs):
            if strs[i].startswith(common):
                i += 1
            else:
                common = common[:-1]
        return common