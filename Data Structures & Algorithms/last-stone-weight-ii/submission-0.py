class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2

        cache = {}

        def dfs(i, curSum):
            if curSum >= target or i == len(stones):
                return abs(curSum - (stoneSum - curSum))

            if (i, curSum) in cache:
                return cache[(i, curSum)]

            cache[(i, curSum)] = min(dfs(i + 1, curSum), dfs(i + 1, curSum + stones[i]))

            return cache[(i, curSum)]  

        return dfs(0, 0)