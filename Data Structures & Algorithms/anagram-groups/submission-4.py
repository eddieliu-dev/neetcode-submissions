class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in anaDict:
                anaDict[key] = []
            anaDict[key].append(s)

        return list(anaDict.values())