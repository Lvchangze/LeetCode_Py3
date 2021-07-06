class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = str(bin(n))
        count = 0
        for i in range(0, len(bin_str)):
            if bin_str[i] == "1":
                count += 1
        return count
