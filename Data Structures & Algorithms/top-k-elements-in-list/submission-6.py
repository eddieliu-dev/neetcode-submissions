class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}

        for n in nums:
            countDict[n] = countDict.get(n, 0) + 1
        
        new_list = list(countDict.keys())
        new_list = sorted(new_list, key=countDict.get, reverse=True)

        return new_list[:k]