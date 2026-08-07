class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       n1=m-1
       n2=n-1
       n3=m+n-1
       while n2>=0:
        if n1>=0 and nums1[n1]>nums2[n2]:
            nums1[n3]=nums1[n1]
            n1-=1
            n3-=1
        else:
            nums1[n3]=nums2[n2]
            n2-=1
            n3-=1