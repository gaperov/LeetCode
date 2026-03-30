class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        cur = (l + r)//2
        while l <= r:
            if nums[cur] < target:
                l = cur + 1
                cur = (l+r)//2
            elif nums[cur] > target:
                r = cur - 1
                cur = (l + r)//2
            else:
                return cur
        return -1
