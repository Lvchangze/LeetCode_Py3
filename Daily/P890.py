from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def string_to_num(string):
            dic = {}
            num = []
            index = 1
            for i in string:
                if i not in dic.keys():
                    dic[i] = index
                    index += 1
            for i in string:
                num.append(dic[i])
            return num
        num_pattern = string_to_num(pattern)
        num_words = [string_to_num(word) for word in words]
        print(num_pattern)
        print(num_words)
        result = []
        for i in range(len(num_words)):
            if num_words[i] == num_pattern:
                result.append(words[i])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAndReplacePattern(
        ["abcdefghijklab", "abcdefghijkabl"], "abcdefghijklab"))
