class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        been = {} # value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in been:
                return [been[diff], i]
            been[n] = i
        return []
        