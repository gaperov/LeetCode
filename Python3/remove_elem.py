class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            del nums[nums.index(val)]
        return len(nums)
