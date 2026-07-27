class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0

        while l < r:
            if nums[l] < nums[r]:
                break
            m = l + (r - l) // 2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        pivot = l

        l, r = 0, len(nums) - 1
        if nums[pivot] == target:
            return pivot
        elif target > nums[pivot] and target <= nums[r]:
            l = pivot + 1
        else:
            r = pivot - 1

        while l <= r:
            m = l + (r - l) // 2
            if target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l if nums[l] == target else -1
