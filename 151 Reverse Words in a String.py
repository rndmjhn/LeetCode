s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"



class Solution:
    def reverseWords(self, s: str) -> str:
        temp = list(s.split(" "))
        i = 0
        while i < len(temp):
            if temp[i] == "":
                temp.pop(i)
            else:
                i += 1
        temp.reverse()
        temp = " ".join(temp)
        return temp




test = Solution()
print(test.reverseWords(s1))
print(test.reverseWords(s2))
print(test.reverseWords(s3))