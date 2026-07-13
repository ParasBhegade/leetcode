class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        result=[]
        for i in range(len(s)):
            num = ""
            for j in range(i, len(s)):
                num += s[j]
                if low <= int(num) <= high:
                    result.append(int(num))
        return sorted(result)