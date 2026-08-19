class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows={}
        for row,seat in reservedSeats:
            if row not in rows:
                rows[row]=set()
            rows[row].add(seat)
        ans=2*(n-len(rows))
        for seats in rows.values():
            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])
            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1
        return ans