from typing import List


class Solution:
    # 词典
    # def findRepeatNumber(self, nums: List[int]) -> int:
    #     hashmap = {}
    #     result = 0
    #     for num in nums:
    #         if num in hashmap.keys():
    #             result = num
    #         else:
    #             hashmap[num] = 0
    #     print(hashmap)
    #     return result

    # hashset
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            if num in hashset:
                return num
            else:
                hashset.add(num)


s = Solution()
s.findRepeatNumber(list([2, 3, 1, 0, 2, 5, 3]))
