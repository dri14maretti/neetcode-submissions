class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("inf")
        L = 0
        size = len(nums)
        currSum = nums[0]
        
        if size == 1:
            return 1 if currSum >= target else 0

        if currSum >= target:
            return 1

        for R in range(1, size):
            currSum += nums[R]
            print(currSum)
            length = R - L + 1
            while currSum >= target:
                minLength = min(length, minLength) 
                currSum -= nums[L]
                L += 1
                length = R - L + 1

        return 0 if minLength == float("inf") else minLength