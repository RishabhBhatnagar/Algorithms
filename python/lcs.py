"""
Find longest common subsequence of two strings.
Example : 
    s1 = mathematics
    s2 = madam
    lcs : mam
"""


def lcs(s1, s2):
    if not s1 or not s2 : return []
    else:
        if s1[0] == s2[0]:
            return [s1[0]] + lcs(s1[1:], s2[1:])
        else : 
            return max(lcs(s1, s2[1:]), lcs(s1[1:], s2))

s = "".join(lcs(input('enter first string : '), input("Enter second string : ")))
print("lcs of two strings is : ", s)
