class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = Counter(chars)
        ans = 0
        for w in words:
            w_cnt = Counter(w)
            good = True
            for c, cnt in w_cnt.items():
                if chars_cnt[c] < cnt:
                    good = False
                    break
            if good:
                ans += len(w)
        return ans

