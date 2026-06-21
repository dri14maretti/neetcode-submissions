class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            # Negativating every value that is available on the array
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res