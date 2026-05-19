class Solution: 
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int: 
        s1=set(nums1) 
        s2=set(nums2) 
        s1=s1.intersection(s2) 
        s1=list(s1) 
        s1.sort() 
        if len(s1)==0: 
            return -1 
        else: 
            return s1[0]