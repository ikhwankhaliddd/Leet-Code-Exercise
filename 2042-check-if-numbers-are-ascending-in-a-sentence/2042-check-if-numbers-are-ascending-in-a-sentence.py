class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        ans = 0
        
        for i in s:
            if i.isdigit():
                if int(i) <= ans:
                    return False
                ans = int(i)
        return True
        