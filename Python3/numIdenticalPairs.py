class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_cnt = {}
        ans = 0
        for num in nums:
            if num in nums_cnt:
                ans += nums_cnt[num]
            nums_cnt[num] = nums_cnt.get(num, 0) + 1
        return ans
