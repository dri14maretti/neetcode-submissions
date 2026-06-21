class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = profit = 0

        for i in range(1, len(prices), 1):
            if prices[buy] > prices[i]:
                buy = i
                continue
                
            profit = max(profit, prices[i] - prices[buy])


        return profit