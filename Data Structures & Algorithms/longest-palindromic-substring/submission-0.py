class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen, maxIdx = 0,0


        for i in range(len(s)):
            # Odd substring
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxIdx = l
                    maxLen = r - l + 1

                l -= 1
                r += 1

            # even substring
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxIdx = l
                    maxLen = r - l + 1

                l -= 1
                r += 1

        return s[maxIdx: maxIdx + maxLen]

