# Given two strings s and t, 
# return true if t is an anagram of s, 
# and false otherwise.

# An Anagram is a word or phrase formed by rearranging 
# the letters of a different word or phrase, typically 
# using all the original letters exactly once.


s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car
if sorted(s) == sorted(t):
    return True