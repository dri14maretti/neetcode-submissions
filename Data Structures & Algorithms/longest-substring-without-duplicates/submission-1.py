class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        L = 0
        maxLength = 1
        size = len(s)

        if size <= 1:
            return size

        visited[s[0]] = 0
        for R in range(1, size):
            if s[R] in visited:
                L = max(visited[s[R]] + 1, L)
            visited[s[R]] = R
            maxLength = max(R - L + 1, maxLength)
                
        return maxLength
