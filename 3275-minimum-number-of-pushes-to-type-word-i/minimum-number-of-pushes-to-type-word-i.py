class Solution:
    def minimumPushes(self, word: str) -> int:
        result=0
        for i in range(len(word)):
            result+= floor(i/8)+1
        return result