st1 = "ABCABC"
st2 = "ABC"
st3 = "ABABAB"
st4 = "ABAB"
st5 = "LEET"
st6 = "CODE"


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])


test = Solution()
print(test.gcdOfStrings(st1, st2))
# print(test.gcdOfStrings(st3, st4))
# print(test.gcdOfStrings(st5, st6))