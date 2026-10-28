class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        li = [-x for x in nums]
        heapq.heapify(li)
        res = 0
        for i in range(k):
            res = heapq.heappop(li)
        
        return -res