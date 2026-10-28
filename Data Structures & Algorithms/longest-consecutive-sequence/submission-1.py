class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        left, right, n = 0, 1, len(nums)
        ans = 0
        if n < 2:
            return n
        while right < n:
            if nums[right - 1] + 1 != nums[right]:
                left = right
            right += 1
            ans = max(ans, right - left)
        
        return ans