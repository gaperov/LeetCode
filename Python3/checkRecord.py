class Solution:
    def checkRecord(self, s: str) -> bool:
        a_cnt = 0
        l_cnt = 0

        if 'LLL' in s:
            return False
        for l in s:
            if l == 'A':
                a_cnt += 1
                if a_cnt > 1:
                    return False

            '''if l == 'L':
                l_cnt += 1
                if l_cnt > 2:
                    return False
            else:
                l_cnt = 0'''

        return True
