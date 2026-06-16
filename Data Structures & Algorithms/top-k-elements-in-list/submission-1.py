class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}

        for n in nums:
            if n not in countDict:
                countDict[n] = 0
            countDict[n]+=1
        
        countDict = dict(sorted(countDict.items(), key=lambda item: item[1], reverse=True))

        res = []

        for num in countDict:
            res.append(num)
            if len(res) == k:
                break
        
        return res
