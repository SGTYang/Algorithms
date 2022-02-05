class Solution:
    def climbStairs(self, n: int) -> int:
        
        dic = {1:1,2:2}
        
        def fibo(n):
            if n not in dic:
                dic[n] = fibo(n-1)+fibo(n-2)
            
            return dic[n]
        
        return fibo(n)
