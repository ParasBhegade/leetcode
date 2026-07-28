class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for i in nums:
            while i>0:
                if i%10==digit:
                    count+=1
                i=i//10
        return count