words1 = "abc"
words2 = "pqr"

words3 = "ab"
words4 = "pqrs"

words5 = "abcd"
words6 = "pq"


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        worda = list(word1)
        wordb = list(word2)
        i = 0
        while i < (len(word1) + len(word2)):
            if i < len(worda):
                output.append(worda[i])
            if i < len(wordb):
                output.append(wordb[i])
            i += 1
        results = map(str, output)
        return "".join(results)

test = Solution()
print(test.mergeAlternately(words1, words2))
print(test.mergeAlternately(words3, words4))
print(test.mergeAlternately(words5, words6))
        