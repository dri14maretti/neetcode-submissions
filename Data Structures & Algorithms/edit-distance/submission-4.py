class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        cache = {}
        def helper(i1, i2):
            if(i1 >= len(word1)):
                return len(word2) - i2

            if(i2 >= len(word2)):
                return len(word1) - i1

            if(i1, i2) in cache:
                return cache[(i1, i2)]

            if (word1[i1] == word2[i2]):
                return helper(i1 + 1, i2 + 1)

            res = min(
                helper(i1, i2 + 1), #insert
                helper(i1 + 1, i2), #delete
                helper(i1 + 1, i2 + 1) #replace
            )

            cache[(i1, i2)] = res + 1

            return cache[(i1, i2)]

        return helper(0,0)