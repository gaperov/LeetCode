class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l, r = 0, len(s)-1
        while l < r:
            if s[l].lower() not in vowels:
                l += 1
                continue
            if s[r].lower() not in vowels:
                r -= 1
                continue
            if s[l].lower() in vowels and s[r].lower() in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
