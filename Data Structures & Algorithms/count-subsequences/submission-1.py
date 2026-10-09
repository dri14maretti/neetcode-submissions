class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {}
        def helper(i, curLen):
            if curLen == len(t):
                return 1
            
            if i >= len(s):
                return 0

            if (i, curLen) in cache:
                return cache[(i, curLen)]

            res = 0
            if s[i] == t[curLen]:
                res += helper(i + 1, curLen + 1)

            res += helper(i + 1, curLen)

            cache[(i, curLen)] = res

            return res

        return helper(0, 0)
