class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        container = [0]*(max(nums)+1)
        
        for i in nums:
            container[i] = container[i]+i
        print(container)
        
        dp = [0]*len(container)
        dp[1] = container[1]
        
        for i in range(2,len(container)):
            dp[i] = max(container[i]+dp[i-2],dp[i-1])
            
        print(dp)
        return dp[-1]
