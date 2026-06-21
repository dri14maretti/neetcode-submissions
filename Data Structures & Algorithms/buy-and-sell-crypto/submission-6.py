class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = profit = 0 

        for i in range(1, len(prices)):
            if prices[i] < prices[left]:
                left = i
            
            profit = max(profit, prices[i] - prices[left])

            
        return profit