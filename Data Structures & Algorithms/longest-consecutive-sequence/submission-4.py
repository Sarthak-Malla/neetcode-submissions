class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        dp = dict()
        longest = 1
        n = len(nums)
        if n == 0:
            return 0
        for i in range(n):
            if nums[i] - 1 in dp:
                longest = dp[nums[i] - 1] + 1
                dp[nums[i]] = longest
            else:
                dp[nums[i]] = 1

        res = 0
        for _, v in dp.items():
            res = max(res, v)
        return res