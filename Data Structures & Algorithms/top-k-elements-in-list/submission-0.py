class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bins = {}
        for num in nums:
            if num not in bins:
                bins[num] = 0
            bins[num] += 1

        keys = bins.keys()
        values = bins.values()

        return [x for _, x in sorted(zip(values, keys))][-k:]