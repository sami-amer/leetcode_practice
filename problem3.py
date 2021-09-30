def lengthOfLongestSubstring(s):
    seen = set()
    count = 0
    counts = []
    for letter in s:
        if letter not in seen:
            count += 1
            seen.add(letter)
        elif letter in seen:
            counts.append(count)    
            count = 0
            seen = set()
    return max(counts)
            




if __name__ == "__main__":
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))