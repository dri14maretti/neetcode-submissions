class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res = "".join(f"{len(string)}#{string}" for string in strs)
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        res=[]
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            res.append(s[l:r])
            l = r
        return res