class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return n
        plus1 = 0
        plus2 = 1
        i = 2
        while i <= n:
            res = plus1 + plus2
            plus1 = plus2
            plus2 = res
            i += 1
        return plus1 + plus2
