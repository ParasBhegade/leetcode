class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            d1={i:s.count(i) for i in s}
            d2={i:t.count(i) for i in t}
            if d1==d2:
                return True
            else:
                return False
        else:
            return False