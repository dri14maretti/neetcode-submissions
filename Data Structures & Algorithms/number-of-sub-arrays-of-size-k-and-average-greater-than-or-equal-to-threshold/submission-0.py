class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        L = 0
        rStart = k - L - 1
        currSum = sum(arr[L:rStart]) # O(k)

        for R in range(rStart, len(arr)): # O(n)
            currSum += arr[R]
            average = currSum / k
            if average >= threshold:
                count += 1
            
            currSum -= arr[L]
            L += 1
        

        return count