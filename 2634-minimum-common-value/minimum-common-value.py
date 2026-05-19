class Solution: 
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int: 
        s1=set(nums1).intersection(set(nums2))
        if s1==set():
            return -1
        else:
            return min(s1)