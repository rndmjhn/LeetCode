s = "A man, a plan, a canal: Panama"
ss = "race a car"
sss = " "



class Solution:
    def isPalindrome(self, s: str) -> bool:
        abc = ''.join(filter(str.isalnum, s)).lower()

        left = 0
        right = len(abc) - 1

        while left < right:
            if abc[left] != abc[right]:
                return False
            left += 1
            right -= 1

        return True
        

test = Solution()
print(test.isPalindrome(s))
print(test.isPalindrome(ss))
print(test.isPalindrome(sss))