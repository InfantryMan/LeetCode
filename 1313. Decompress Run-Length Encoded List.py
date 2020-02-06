class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            count = nums[i]
            number = nums[i + 1]
            for i in range(count):
                res.append(number)
        return res