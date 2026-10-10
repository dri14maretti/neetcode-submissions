class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        cache = {}

        def helper(i1, i2):
            if len(s3) != (len(s1) + len(s2)):
                return False
            
            if i1 >= len(s1):
                return s2[i2:] == s3[(i1+i2):]

            if i2 >= len(s2):
                return s1[i1:] == s3[(i1+i2):]

            if (i1, i2) in cache:
                return cache[(i1, i2)]

            res = False
            if s1[i1] == s3[i1 + i2]:
                res = res or helper(i1 + 1, i2)
            if s2[i2] == s3[i1 + i2]:
                res = res or helper(i1, i2 + 1)
            if s1[i1] != s3[i1 + i2] and s2[i2] != s3[i1 + i2]:
                return False

            cache[(i1, i2)] = res

            return cache[(i1, i2)]

        return helper(0,0)