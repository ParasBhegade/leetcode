class Solution:
    def totalNumbers(self, digits):
        n = len(digits)
        set1 = set()

        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k and digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        set1.add(num)

        return len(set1)