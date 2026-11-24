class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        n = len(prices)
        for i in range(n):
            for j in range(i+1 , n):
                total = prices[j] - prices[i]

                profit = max(total , profit)
        
        return profit