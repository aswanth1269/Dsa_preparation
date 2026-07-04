class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            SortedS = ''.join(sorted(s))
            res[SortedS].append(s)
        return list(res.values())
