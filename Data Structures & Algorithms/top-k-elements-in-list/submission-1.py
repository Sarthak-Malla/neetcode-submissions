class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        maxheap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(maxheap)
        ksmallest = heapq.nsmallest(k, maxheap)
        return [i for _, i in ksmallest]