class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        box = [0]*(max(nums)+1)
        
        for i in nums:
            box[i] = box[i]+i
        
        dp = [0]*len(box)
        dp[1] = box[1]
        
        for i in range(2,len(box)):
            dp[i] = max(box[i]+dp[i-2],dp[i-1])
            
        print(dp)
        return dp[-1]
