class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        i = 0

        while i < n:
            curr = nums[i]
            l, r = i + 1, n - 1
            while l < r:
                s = curr + nums[l] + nums[r]
                if s == 0:
                    res.add((curr, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1

            i += 1
        return [list(x) for x in res]
