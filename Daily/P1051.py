from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = heights.copy()
        list.sort(heights)
        print(heights_sorted)
        n = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                n += 1
        return n


if __name__ == "__main__":
    sol = Solution()
    print(sol.heightChecker([1, 1, 4, 2, 1, 3]))
