class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dfs(i, rest):
            if rest == 0:
                return 0
            
            if i == len(coins):
                return sys.maxsize

            if (i, rest) in cache:
                return cache[(i, rest)]

            res = dfs(i + 1, rest)

            if rest - coins[i] >= 0:
                take = dfs(i, rest - coins[i])
                if take != sys.maxsize:
                    res = min(res, take + 1)

            cache[(i, rest)] = res
            
            return cache[(i, rest)]
        
        response = dfs(0, amount)
        
        return response if response < sys.maxsize else -1