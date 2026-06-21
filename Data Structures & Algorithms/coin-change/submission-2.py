class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for aCount in range(1, amount + 1):
            for coin in coins:
                if aCount - coin >= 0:
                    dp[aCount] = min(dp[aCount], 1 + dp[aCount - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1
        