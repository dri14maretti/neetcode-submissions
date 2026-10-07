class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        cache = {}
        
        def countZerosAndOnes(element):
            zeros, ones = 0, 0
            for c in element:
                if c == '0':
                    zeros += 1
                else:
                    ones += 1

            return (zeros, ones)

        def dfs(i, zerosLeft, onesLeft):
            if i >= len(strs):
                return 0

            if (i, zerosLeft, onesLeft) in cache:
                return cache[(i, zerosLeft, onesLeft)]

            (zeros, ones) = countZerosAndOnes(strs[i])
            
            res = dfs(i + 1, zerosLeft, onesLeft)
            if zerosLeft >= zeros and onesLeft >= ones:
                res = max(res, 1 + dfs(i + 1, zerosLeft - zeros, onesLeft - ones))

            cache[(i, zerosLeft, onesLeft)] = res
            return res

        return dfs(0, m, n)