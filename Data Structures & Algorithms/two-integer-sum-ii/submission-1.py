class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        s = numbers
        l, r = 0, n - 1
        while l <= r:
            while l + 1 < n and s[l + 1] == s[l]:
                l += 1
            while r - 1 >= 0 and s[r - 1] == s[r]:
                r -= 1
            sum_ = s[l] + s[r]
            if sum_ == target:
                return [l + 1, r + 1] if l + 1 < r + 1 else [r + 1, l + 1]
            elif sum_ < target:
                l += 1
            else:
                r -= 1
        return []