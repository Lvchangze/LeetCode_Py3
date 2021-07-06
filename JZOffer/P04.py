from typing import List


class Solution:
    # 找到合适的子矩阵
    # def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    #     n = len(matrix)
    #     if n == 0:
    #         return False
    #     m = len(matrix[0])
    #     if m == 0:
    #         return False
    #     n_cut = n
    #     m_cut = m
    #     if n == 0 or m == 0:
    #         return False
    #     for i in range(0, m):
    #         if matrix[0][i] > target:
    #             m_cut = i
    #     for i in range(0, n):
    #         if matrix[i][0] > target:
    #             n_cut = i
    #     for i in range(0, n_cut):
    #         for j in range(0, m_cut):
    #             if matrix[i][j] == target:
    #                 return True
    #     return False

    # 从右上角（或左下角）开始查找
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        i = 0
        j = m-1
        while j >= 0 and i < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
