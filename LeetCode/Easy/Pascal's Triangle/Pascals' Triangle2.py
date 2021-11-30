class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        dp = [[1 for _ in range(i+1)] for i in range(numRows)]
        
        for i in range(2,len(dp)):
            for j in range(1,len(dp[i])-1):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        
        return dp
