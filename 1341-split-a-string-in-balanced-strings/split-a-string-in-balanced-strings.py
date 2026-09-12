class Solution:
    def balancedStringSplit(self, s: str) -> int:
        temp = 0
        res = 0
        for i in s:
            if i == 'R':
                temp += 1
            else:
                temp -= 1
            if temp == 0:
                res += 1
        return res