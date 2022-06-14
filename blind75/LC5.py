def longestPalindrome(s):
    res = ''

    for i in range(len(s)):
        # if odd resulting string
        str_o = expandFromMiddle(s,i,i)
        if len(str_o) > len(res):
            res = str_o
        
        str_e = expandFromMiddle(s,i,i+1)
        if len(str_e) > len(res):
            res = str_e

def expandFromMiddle(s,l,r):
    while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


if __name__ == '__main__':
    input1 = "babad"
    input2 = "cbbd"
    input3 = "a"
    input4 = "ac"
    print(longestPalindrome(input2))