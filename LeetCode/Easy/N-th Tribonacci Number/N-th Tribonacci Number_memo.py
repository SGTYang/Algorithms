class Solution:
    def tribonacci(self, n: int, memo={}) -> int:
        
        if n == 0:
            return 0
        if n <3:
            return 1
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)
            return memo[n]
