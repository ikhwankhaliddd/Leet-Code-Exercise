class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans = []
        
        for i in range(len(sentences)):
            x = sentences[i].split(' ')
            x = len(x)
            ans.append(x)
        return max(ans)