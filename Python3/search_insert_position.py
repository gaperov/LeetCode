class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            i = 0
            j = len(nums)-1
            while(i <= j):
                if target < nums[i]:
                    return i
                else:
                    i += 1
                if target > nums[j]:
                    return j+1
                else:
                    j-=1
            return i
                

