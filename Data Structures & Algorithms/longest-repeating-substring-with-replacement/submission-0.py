class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 1
        count = {}
        l = 0

        for r in range(len(s)): # O(26n) -> O(n)
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k: # max(count.values()) -> O(26)
                count[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen