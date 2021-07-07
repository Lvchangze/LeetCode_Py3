class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ""
        for i in range(0, len(s)):
            if s[i] == " ":
                res += "%20"
            else:
                res += s[i]
        return res

    def replaceSpace2(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ':
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)



solution = Solution()
print(solution.replaceSpace("We are Place"))
