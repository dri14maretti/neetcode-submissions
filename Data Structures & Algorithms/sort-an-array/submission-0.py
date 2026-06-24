class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counter = [0] * 10**6

        for num in nums:
            counter[num + 50000] += 1

        result = []

        for i in range(len(counter)):
            for _ in range(counter[i]):
                result.append(i - 50000)

        return result