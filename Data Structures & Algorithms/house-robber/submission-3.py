class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) < 3:
            nums.append(0)
            return max(nums[0] + nums[2], nums[1])

        dp = nums[:2]
        dp.append(nums[0] + nums[2])

        for i in range(3, len(nums)):
            summed = max(dp[1], dp[0])
            
            dp[0], dp[1], dp[2] = dp[1], dp[2], summed + nums[i]

        return max(dp[1], dp[2])

