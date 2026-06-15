class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        been = {}

        for i in range(len(nums)):
            if been.get(target-nums[i], -1) != -1:
                return [been[target-nums[i]], i]
            been[nums[i]] = i
        return []