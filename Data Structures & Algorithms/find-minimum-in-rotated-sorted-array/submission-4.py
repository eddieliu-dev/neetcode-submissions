class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minn = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                return min(minn, nums[l])
            m = l + (r - l) // 2
            minn = min(minn, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return minn
