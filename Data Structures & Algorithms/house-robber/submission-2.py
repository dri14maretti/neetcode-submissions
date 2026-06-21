class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = dp2
            dp2 = max(temp, dp1 + nums[i])
            dp1 = temp

        return dp2