class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        max = len(numbers) - 1
        min = 0

        while True:
            if numbers[min] + numbers[max] > target:
                max -= 1
            elif numbers[min] + numbers[max] < target:
                min += 1
            else:
                return [min+1, max+1]
