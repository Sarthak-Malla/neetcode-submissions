class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceMap = {}
        minHeap = []
        heapq.heapify(minHeap)

        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            if distance not in distanceMap:
                distanceMap[distance] = []
            distanceMap[distance].append(point)
            heapq.heappush(minHeap, distance)
        
        res = []
        while minHeap:
            d = heapq.heappop(minHeap)
            if k == 0:
                break
            res.append(distanceMap[d][0])
            del distanceMap[d][0]
            k -= 1
        
        return res