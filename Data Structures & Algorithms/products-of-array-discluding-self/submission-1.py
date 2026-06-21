class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, res = [0] * len(nums), [0] * len(nums)
        
        prefixProd = 1
        for i in range(len(nums)):
            prefix[i] = prefixProd
            prefixProd *= nums[i]

        postfixProd = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = postfixProd * prefix[j] 
            postfixProd *= nums[j]

        return res

        