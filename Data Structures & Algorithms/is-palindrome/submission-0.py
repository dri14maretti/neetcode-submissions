class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while(right > left):
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1

            if(s[left].lower() != s[right].lower()):
                return False
            
            right -= 1
            left += 1

        return True

        