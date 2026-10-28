class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dp = dict()
        for s in strs:
            key = "".join(sorted(s))

            if key in dp:
                dp[key].append(s)
            else:
                dp[key] = [s]
        
        return [v for _, v in dp.items()]