class Solution:
    def minPartitions(self, n: str) -> int:
        digit=0
        for i in n:
            if int(i)>digit:
                digit=int(i)
        return digit