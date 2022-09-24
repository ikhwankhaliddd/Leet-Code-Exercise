class Solution:
    def isValid(self, s: str) -> bool:
        
        hashMap = {'[' : ']',
                  '(' : ')',
                  '{' : '}'}
        
        ans = []
        
        for i in s :
            if i in hashMap:
                ans.append(i)
            elif len(ans) == 0 or hashMap[ans.pop()] != i:
                return False
        return len(ans) == 0
        