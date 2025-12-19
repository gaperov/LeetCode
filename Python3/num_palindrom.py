class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        n = len(str_num)
        if str_num == str_num[::-1]:
            return True
        else:
            return False