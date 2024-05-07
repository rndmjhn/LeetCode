s1 = "()"
s2 = "()[]{}"
s3 = "(]"


 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if bracket in sets:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != sets[stack.pop()]:
                return False
            
        return len(stack) == 0
    

test = Solution()
print(test.isValid(s1))
print(test.isValid(s2))
print(test.isValid(s3))