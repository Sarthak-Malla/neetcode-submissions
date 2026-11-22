class Solution:
    def targetSum(self, arr, target):
        # assuming arr is sorted
        l, r = 0, len(arr) - 1
        res = set()

        while l < r:
            s = arr[l] + arr[r]
            if s == target:
                if (arr[l], arr[r]) not in res:
                    res.add((arr[l], arr[r]))
                l += 1
                r -= 1
            elif s > target:
                r -= 1
            else:
                l += 1
            
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        seen = set()

        for i in range(n):
            other = self.targetSum(nums[i+1:], -nums[i])
            if nums[i] in seen:
                continue
            
            seen.add(nums[i])
            if len(other) != 0:
                for item in other:
                    res.append([nums[i], *item])
        
        return res