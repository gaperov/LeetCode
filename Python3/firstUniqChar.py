class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = dict()
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]][1] += 1
            else:
                letters |= {s[i]:[i,1]} 
        for val in letters.values():
            if val[1] == 1:
                return val[0]
        return -1
            
