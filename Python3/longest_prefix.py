class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        flag = True
        while (len(s) > 0 and flag):
            count = 0
            for word in strs:
                if word.find(s) == 0:
                    count += 1
            if count == len(strs):
                flag = False
            else:
                s = s[:len(s)-1]
        return s
