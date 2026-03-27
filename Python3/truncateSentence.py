class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaces = 0
        ans = ''
        for c in s:
            if c == ' ':
                spaces += 1
            if spaces == k:
                return ans
            ans += c
        return ans
