class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for i in range(1,n+1):
            if i % 5 == 0 and i % 3 == 0:
                res = "FizzBuzz"
            elif i % 3 == 0 :
                res = "Fizz"
            elif i % 5 == 0 :
                res = "Buzz"
            else:
                res = str(i)
                
            ans.append(res)
        return ans