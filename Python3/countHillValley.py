class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        def is_hill_valley(l, r):
            while l >= 0 and r < len(nums):
                if nums[l] == nums[i]:
                    l -= 1
                    continue
                if nums[r] == nums[i]:
                    r += 1
                    continue
                if (nums[r] > nums[i] and nums[l] > nums[i]) or \
                    (nums[r] < nums[i] and nums[l] < nums[i]):
                    return 1
                else:
                    return 0
            return 0

        ans = 0
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l, r = i-1, i+1
            ans += is_hill_valley(l, r)
            

        return ans

