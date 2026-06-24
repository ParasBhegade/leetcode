class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)+1
        if n==0:
            return []
        else:
            l=[]
            s=set(nums)
            for i in range(1,n):
                if i not in s:
                    l.append(i)
        return l