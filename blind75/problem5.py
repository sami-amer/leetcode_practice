def longestPalindrome(s):
    matrix = [[False for _ in range(len(s))] for _ in range(len(s))] # Make matrix of solutions, where TRUE indicated S[i:j] is a palindrome
    for i in range(len(s)):
        matrix[i][i] = True
    max_len = 1
    start = 0
    for l in range(2,len(s) + 1): #loop over lengths
        for i in range(len(s) - l + 1): #loop over start points
            end = i + l
            if l == 2:
                if s[i] == s[end - 1]:
                    matrix[i][end-1] = True
                    max_len = l
                    start = i
            else:
                if s[i] == s[end-1] and matrix[i + 1][end-2]:
                    matrix[i][end-1] = True
                    max_len = l
                    start = i
    return s[start:start+max_len]



if __name__ == '__main__':
    input1 = "babad"
    input2 = "cbbd"
    input3 = "a"
    input4 = "ac"
    print(longestPalindrome(input2))