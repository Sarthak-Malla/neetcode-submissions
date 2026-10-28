class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not len(strs):
            return [[]]

        bins = {}
        bins[''.join(sorted(strs[0]))] = []

        for s in strs:
            sor = ''.join(sorted(s))
            if bins.get(sor) != None:
                bins[sor].append(s)
            else:
                bins[sor] = [s]

        res = []
        for key in bins:
            res.append(bins[key])
        
        return res
