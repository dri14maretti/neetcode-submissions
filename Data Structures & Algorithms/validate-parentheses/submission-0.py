class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesStack = []
        pairsHash = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        for c in s:
            if(c == "{" or c == "(" or c == "["):
                parenthesesStack.append(c)
                continue;
            

            if(len(parenthesesStack) == 0 or c != pairsHash[parenthesesStack.pop()]):
                return False

        return len(parenthesesStack) == 0
        