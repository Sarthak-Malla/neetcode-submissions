class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for s in strs:
            ss = "".join(sorted(s))
            store[ss].append(s)
        
        return [x for x in store.values()]
                