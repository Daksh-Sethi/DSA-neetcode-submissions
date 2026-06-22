class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            d.setdefault("".join(sorted(word)), []).append(word)
        return list(d.values())
