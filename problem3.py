def lengthOfLongestSubstring(s, count = 0, counts = set()):
    if not s:
        return counts
    seen = set()
    for letter in s:
        if letter not in seen:
            count += 1
            seen.add(letter)
        elif letter in seen:
            counts.add(count)    
            count = 0
            # seen = set(letter)
            lengthOfLongestSubstring(s[1:], count, counts)
    # counts.add(count)
    
    return counts
            




if __name__ == "__main__":
    s = "pwwkew"
    s2 = "dvdf"
    s3 = "bbbbb"
    print(lengthOfLongestSubstring(s3))