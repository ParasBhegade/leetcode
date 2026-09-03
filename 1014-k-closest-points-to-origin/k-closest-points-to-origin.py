class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        target=k-1
        def dist(point):
            return point[0]**2+point[1]**2
        def part(points,low,high):
            pivot=points[low]
            i,j=low,high
            while i<j:
                while i<=high-1 and dist(points[i])<=dist(pivot):
                    i+=1
                while j>=low+1 and dist(points[j])>dist(pivot):
                    j-=1
                if i<j:
                    points[i],points[j]=points[j],points[i]
            points[j],points[low]=points[low],points[j]
            return j
        low=0
        high=len(points)-1
        while low<high:
            pi=part(points,low,high)
            if pi==target:
                break
            elif pi<target:
                low=pi+1
            else:
                high=pi-1
        return points[:k]