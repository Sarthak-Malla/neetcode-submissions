class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        df = defaultdict(int)
        for num in nums:
            df[num] += 1
        
        heap = [(-count, value) for value, count in df.items()]
        heapq.heapify(heap)

        res = []
        for i in range(k):
            _, value = heapq.heappop(heap)
            res.append(value)
        
        return res