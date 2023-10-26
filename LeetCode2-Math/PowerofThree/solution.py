class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        result = math.log(n) / math.log(3)

        return abs(result - round(result)) < 1e-10


