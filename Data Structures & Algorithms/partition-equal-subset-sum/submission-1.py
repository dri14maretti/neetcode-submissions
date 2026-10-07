class Solution:
    def subsetSum(self, nums, i, curSum, target, cache):
        if i == len(nums) - 1:
            return False
        
        newSum = curSum + nums[i]
        if newSum == target:
            return True

        complement = target - curSum

        if cache[i][complement] != -1:
            return cache[i][complement]

        cache[i][complement] = self.subsetSum(nums, i + 1, curSum , target, cache) or self.subsetSum(nums, i + 1, newSum , target, cache)

        if newSum > target:
            newSum = curSum

        return cache[i][complement]
    def canPartition(self, nums: List[int]) -> bool:
        arrayTotal = sum(nums)

        if arrayTotal % 2 > 0:
            return False
        
        target = arrayTotal // 2

        cache = [[-1] * (target + 1) for _ in range(len(nums) + 1)]

        return self.subsetSum(nums, 0, 0, target, cache)