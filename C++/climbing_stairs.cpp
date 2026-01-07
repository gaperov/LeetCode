class Solution {
public:
    int climbStairs(int n) {
         if (n < 4) return n;

         int plus1 = 3;
         int plus2 = 2;
         int res = 0;

         for (int i = 4; i <= n;i++) {
            res = plus1 + plus2;
            plus2 = plus1;
            plus1 = res;
         }
         return res;
    }
};
