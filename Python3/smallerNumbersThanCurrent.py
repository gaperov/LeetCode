class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        nums_sorted = sorted(nums)
        nums_idx = {}
        for i, num in enumerate(nums_sorted):
            if num not in nums_idx:
                nums_idx[num] = i
        for num in nums:
            ans.append(nums_idx[num])
        return ans
