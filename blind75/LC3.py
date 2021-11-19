def lengthOfLongestSubstring(s):
    tmp = ''
    counts = set()
    for letter in s:
        if letter not in tmp:
            tmp += letter
        else:
            counts.add(len(tmp))
            tmp = tmp[tmp.index(letter)+1:] + letter  # ! This indexing was the biggest difference between my solution and the working solution.
    counts.add(len(tmp))
    return max(counts)
            




if __name__ == "__main__":
    s = "pwwkew"
    s2 = "dvdf"
    s3 = "bbbbb"
    s4 = "aab"
    print(lengthOfLongestSubstring(s2))