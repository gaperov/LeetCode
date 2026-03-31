class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)

        l, r = 0, n
        while l < r:
            mid = (l+r)//2
            if mid < nums[mid]:
                l = mid + 1
            else:
                r = mid
        return -1 if l < len(nums) and l == nums[l] else l
