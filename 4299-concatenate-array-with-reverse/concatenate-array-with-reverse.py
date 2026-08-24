class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev=nums[::-1]
        return nums+rev