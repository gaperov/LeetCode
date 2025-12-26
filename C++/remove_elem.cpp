class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.empty()) return 0;

        int k = 0;
        int j = nums.size() - 1;
        for (int i = 0; i<j+1; i++) {
            if (nums[i] == val) {
                nums[i] = nums[j];
                i--;
                j--;
                k++;
            }
        }
        return nums.size()-k;
    }
};
