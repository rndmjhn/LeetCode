s1 = "abc"
t1 = "ahbgdc"
s2 = "axc"
t2 = "ahbgdc"


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ss, tt = 0, 0

        while ss < len(s) and tt < len(t):
            if s[ss] == t[tt]:
                ss += 1
            tt += 1
        
        return ss == len(s)

                
        

test = Solution()
print(test.isSubsequence(s1, t1))
print(test.isSubsequence(s2, t2))