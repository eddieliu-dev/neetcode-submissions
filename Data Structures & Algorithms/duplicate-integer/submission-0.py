class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0;
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count+=1;
                if count > 1:
                    return True;
            count = 0
        return False;