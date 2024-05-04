from posixpath import split
from pydoc import ispackage

class Solution:
    def isPalindrome(x):
        xStr = list(str(x))
        Strx = xStr.copy()
        Strx.reverse()

        if xStr == Strx:
            return True
        else:
            return False


    resultant = isPalindrome(12321)
    print(resultant)
