class Solution:
    def reverseWords(self, s: str) -> str:
        rs=''
        for i in s:
            for j in i:
                rs=j+rs
        rs=rs.split()
        rs.reverse()
        rs = " ".join(rs)
        return rs