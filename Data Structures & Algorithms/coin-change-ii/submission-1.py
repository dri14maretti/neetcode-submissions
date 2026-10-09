class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, amountLeft):
            if i >= len(coins):
                return 0

            if amountLeft == 0:
                return 1

            if (i, amountLeft) in cache:
                return cache[(i, amountLeft)]

            res = dfs(i + 1, amountLeft)

            newAmount = amountLeft - coins[i]
            if newAmount >= 0:
                res += dfs(i, amountLeft - coins[i])

            cache[(i, amountLeft)] = res

            return cache[(i, amountLeft)]

        return dfs(0, amount)