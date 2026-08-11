class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newNums = [-x for x in nums]
        heapq.heapify(newNums)

        result = 0
        while k > 0:
            result = -heapq.heappop(newNums)
            k -= 1

        return result