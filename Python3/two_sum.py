class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            need_for_sum = target - nums[i]
            if need_for_sum in numMap:
                return [numMap[need_for_sum], i]
            numMap[nums[i]] = i
        return []