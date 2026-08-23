class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        half=n//2
        part1=num[:half]
        part2=num[half:]
        s1=sum(int(i) for i in part1 if i!="?")
        s2=sum(int(i) for i in part2 if i!="?")
        c1=part1.count("?")
        c2=part2.count("?")
        count=c1+c2
        if count%2==1:
            return True
        diff=s1-s2
        rc=c1-c2
        return diff+9*rc//2!=0