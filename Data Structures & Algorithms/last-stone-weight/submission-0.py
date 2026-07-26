class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, (-1 * stone, None))

        while len(pq) > 1:
            stoneX, _ = heapq.heappop(pq)
            stoneY, _ = heapq.heappop(pq)

            if(stoneX == stoneY):
                continue
            
            newStone = stoneX - stoneY
            heapq.heappush(pq, (newStone, None))

        if len(pq) == 1:
            stone, _ = heapq.heappop(pq)
            return -1 * stone
        else:
            return 0

        return -1 * pq[0] if len(pq) == 1 else 0