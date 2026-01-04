class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int i = a.size()-1;
        int j = b.size()-1;
        int hold = 0;
        while(i >= 0 || j >= 0 || hold) {
            if (i >= 0) hold += a[i--] - '0';
            if (j >= 0) hold += b[j--] - '0';
            res += hold % 2 + '0';
            hold /= 2;
        }
        reverse(begin(res), end(res));
        return res;
    }
};
