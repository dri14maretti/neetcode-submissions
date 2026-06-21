class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = {}

        for num in nums:
            frequencyDict[num] = 1 + frequencyDict.get(num, 0)

        heap = []

        for num in frequencyDict.keys():
            heapq.heappush(heap, (frequencyDict[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        