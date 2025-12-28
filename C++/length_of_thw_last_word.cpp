class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        int res = 1;
        for(int i = s.length()-1; i > 0;i--){
            if (s[i] != ' '){
                count += 1;
                if (s[i-1] == ' '){
                    res = count;
                    break;
                } else {
                    res = count + 1;
                }
            }
        }
        return res;
    }
};
