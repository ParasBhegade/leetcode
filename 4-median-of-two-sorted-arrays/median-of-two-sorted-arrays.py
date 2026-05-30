class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n3=sorted(nums1+nums2)
        median=0
        if  len(n3)%2==0:
            mid1=n3[int(len(n3)/2)-1]
            mid2=n3[int((len(n3)/2))]
            median=(mid1+mid2)/2
        else:
            median=n3[int(len(n3)/2)]
        return median