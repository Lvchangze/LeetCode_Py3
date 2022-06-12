class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        l_ones, r_zeros = [0] * n, [0] * n
        one = 0
        for i in range(n):
            l_ones[i] = one
            if s[i] == "1":
                one += 1
        zero = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                zero += 1
            r_zeros[i] = zero
        dp = [0] * n
        for i in range(n):
            dp[i] = l_ones[i] + r_zeros[i]
        return min(min(dp), one, zero)
