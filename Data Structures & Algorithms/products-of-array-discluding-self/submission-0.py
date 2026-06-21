class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zerosIndex = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zerosIndex.append(i)
                continue

            product *= nums[i]

        result = [0] * len(nums)
        if len(zerosIndex) == 0:
            for i in range(len(nums)):
                result[i] = (int) (product / nums[i]) 
        elif len(zerosIndex) == 1:
            result[zerosIndex[0]] = product        

        return result

        