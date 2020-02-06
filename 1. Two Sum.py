class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for index, number in enumerate(nums):
            if (target - number) not in sums:
                sums[number] = index
            else:
                return [sums[target - number], index]
        