from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if(len(piles) == h):
            return max(piles)
        _min = 1
        _max = max(piles)
        while(_min < _max):
            mid = (_min + _max)/2
            # print(_min,_max,mid)

            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile/mid)

            if(total_hour > h):
                _min = mid + 1
            else:
                _max = mid
        return _min


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3,7,6,11], 8))
