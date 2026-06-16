class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}

        for n in nums:
            if n not in countDict:
                countDict[n] = 0
            countDict[n] += 1

        new_list = list(countDict.keys())
        new_list.sort(key = countDict.get, reverse=True)

        return new_list[:k]
