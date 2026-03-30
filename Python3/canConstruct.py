class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_cnt = Counter(magazine)
        for c in ransomNote:
            if c not in magazine_cnt:
                return False
            magazine_cnt[c] -= 1
            if magazine_cnt[c] == -1:
                return False
        return True

'''
faster
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_cnt = Counter(magazine)
        for c in ransomNote:
            if c not in magazine_cnt:
                return False
            magazine_cnt[c] -= 1
            if magazine_cnt[c] == -1:
                return False
        return True
'''
