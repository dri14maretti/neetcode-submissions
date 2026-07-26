class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        greatestSequence = 0
        for num in nums:
            if num - 1 not in numSet:
                sequenceLen = 0
                while (num + sequenceLen) in numSet:
                    sequenceLen += 1

                greatestSequence = max(greatestSequence, sequenceLen)

        return greatestSequence