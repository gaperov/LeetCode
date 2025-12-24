class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string s = strs[0];
        bool flag = true;
        int n = s.length();
        while(n>0 && flag){
            int count = 0;
            for(int i = 0; i < strs.size(); i++) {
                if (strs[i].find(s) == 0){
                    count += 1;
                }
            }
            if (count == strs.size()){
                flag = false;
            } else {
                n -= 1;
                s = s.substr(0, n);
            }
        }
        return s;
    }
};
