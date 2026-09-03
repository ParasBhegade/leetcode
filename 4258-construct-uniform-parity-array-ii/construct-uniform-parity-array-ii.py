class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini= min(nums1)
        if mini%2!=0:
            return True
        for i in nums1:
            if i%2!=0:
                return False
        return True
