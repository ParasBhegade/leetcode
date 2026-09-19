class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        prev = 0
        for num in pref:
            res.append(prev ^ num)
            prev = num
        return res