class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        arr = []
        while x > 0:
            arr.append(x % 10)
            x //= 10

        i = 0
        j = len(arr) - 1

        print(arr)

        while i < j:
            print(i, j)
            if arr[i] != arr[j]:
                return False

            i += 1
            j -= 1

        return True