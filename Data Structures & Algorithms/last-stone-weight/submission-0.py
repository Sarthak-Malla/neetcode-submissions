class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            print(x, y)

            if x == y:
                continue
            
            print(-(abs(abs(x) - abs(y))))
            heapq.heappush(maxHeap, -(abs(abs(x) - abs(y))))
        
        return 0 if len(maxHeap) == 0 else maxHeap[0] * -1