class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        i = len(a)-1
        j = len(b)-1
        hold = 0
        while i>=0 or j>=0 or hold:
            if i >= 0: hold += (int(a[i]))
            if j >= 0: hold += (int(b[j]))
            res += (str(hold%2))
            hold //= 2
            i -= 1
            j -= 1
        return res[::-1]
