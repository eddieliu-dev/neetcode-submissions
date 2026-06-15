class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {} # Store nums needed later with index
        for i, n in enumerate(nums):
            if n in need:
                return [need[n], i]
            need[target-n] = i
            