class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for n in range(i + 1, len(nums)):
                if nums[n] + nums[i] == target:
                    return [i, n]
        