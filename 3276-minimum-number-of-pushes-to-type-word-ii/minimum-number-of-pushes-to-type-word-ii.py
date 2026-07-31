class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            d[i] = d.get(i, 0) + 1
        freq=sorted(list(d.values()),reverse=True)
        result=0
        for i in range(len(freq)):
            result+=freq[i]*((i//8)+1)
        return result

