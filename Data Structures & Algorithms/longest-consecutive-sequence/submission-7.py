class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        df = defaultdict(int)

        # creating the starts
        for num in nums_set:
            if num - 1 not in nums_set:
                start = num
                while start in nums_set:
                    df[num] += 1
                    start += 1
                
        return max(df.values()) if df.values() else 0
