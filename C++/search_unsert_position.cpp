class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size() - 1;
        while(i <= j){
            if (target <= nums[i]){
                return i;
            } else {
                i += 1;
            }
            if (target > nums[j]){
                return j + 1;
            } else {
                j -= 1;
            }
        }
        return i;
    }
};
