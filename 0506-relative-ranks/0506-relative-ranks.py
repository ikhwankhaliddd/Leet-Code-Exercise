class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        res = []
        scoreSort = sorted(score,reverse = True)
        
        for i in score:
            if scoreSort.index(i) == 0:
                res.append("Gold Medal")
            elif scoreSort.index(i) == 1:
                res.append("Silver Medal")
            elif scoreSort.index(i) == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(scoreSort.index(i) + 1))
        return res