class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strHash = {}
        res = []

        for string in strs:
            orderStr = "".join(sorted(string))
            
            if orderStr in strHash:
                res[strHash[orderStr]].append(string)
            else:
                res.append([string])
                strHash[orderStr] = len(res) - 1
        
        return res