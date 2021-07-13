from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []

        def dfs(index):
            if index == len(c) - 1:  # 如果固定了最后一位，说明这条路的递归已经停止
                res.append(''.join(c))  # 添加排列方案
                return

            dic = set()
            for i in range(index, len(c)):
                if c[i] in dic:  # 重复，因此剪枝
                    continue
                dic.add(c[i])
                c[i], c[index] = c[index], c[i]  # 交换，将 c[i] 固定在第 index 位
                dfs(index + 1)  # 开启固定第 x + 1 位字符
                c[i], c[index] = c[index], c[i]  # 恢复交换

        dfs(0)
        return res

