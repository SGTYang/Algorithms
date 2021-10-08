class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        price_again = []
        
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                
                price_again.append(prices[i+1]-prices[i])
                
        return sum(price_again)
