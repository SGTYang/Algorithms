class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {1:1,2:2}
        
        def climb(n):
            print(dic)
            if n not in dic:
                dic[n] = climb(n-1) + climb(n-2)
            return dic[n]
        
        return climb(n)
