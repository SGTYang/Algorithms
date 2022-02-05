class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0]*len(nums)
        if len(nums)>2:
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[0]+nums[2]

            for i in range(3,len(nums)):
                dp[i] = max(dp[i-2]+nums[i],dp[i-3]+nums[i])
        else:
            return max(nums)
        return max(dp)
