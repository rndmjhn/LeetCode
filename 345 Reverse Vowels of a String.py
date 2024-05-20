s1 = "hello"       # Output: "holle"
s2 = "leetcode"    # Output: "leotcede"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


class Solution:
    def reverseVowels(self, s: str) -> str:
        markers = []
        stack = []
        i = 0
        for i in range(len(s)):
            if s[i] in vowels:
                stack.insert(0, s[i])
                markers.append(i)

        temp = list(s)
        for j in markers:
            temp[j] = stack.pop(0)
        
        s = "".join(map(str, temp))
        return s

test = Solution()
print(test.reverseVowels(s1))
print(test.reverseVowels(s2))