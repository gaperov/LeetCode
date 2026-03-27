class Solution:
    def interpret(self, command: str) -> str:
        '''return command.replace('()', 'o').replace('(al)', 'al')'''

        ans = ''
        tmp = ''
        for char in command:
            tmp += char
            if tmp == 'G':
                ans += 'G'
                tmp = ''
            elif tmp == '()':
                ans += 'o'
                tmp = ''
            elif tmp == '(al)':
                ans += 'al'
                tmp = ''
        
        return ans
