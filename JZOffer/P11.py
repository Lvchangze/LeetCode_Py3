from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        length = len(numbers)
        i = 0
        j = length - 1
        while i < j:
            m = (i + j) // 2  # 整除
            if numbers[m] < numbers[j]:
                j = m
            elif numbers[m] > numbers[j]:
                i = m + 1
            else:
                j -= 1
        return numbers[i]
