class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        n = 10
        arr = [math.floor(x % n / (n / 10))]
        
        while math.floor(x / n) > 0:
            n *= 10
            arr.append(math.floor(x % n / (n / 10)))

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