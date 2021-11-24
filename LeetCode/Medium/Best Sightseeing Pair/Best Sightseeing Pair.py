class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0]*len(values)
        dp[0] = values[0]
        max_value = 0
        
        for i in range(1,len(values)):
            dp[i] =  max(dp[i-1], values[i-1]+i-1)
            max_value = max(dp[i]+values[i]-i,max_value)
        
        return max_value
