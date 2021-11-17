from typing import DefaultDict, List
# import numpy as np
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make word list
        # order and tuple
        # tuple(sorted(list(word))) -> key
        # map words to this key, and store as a list
        # return all values

        tuplesToWords = DefaultDict(lambda: [])
        for word in strs:
            key = tuple(sorted(list(word)))
            tuplesToWords[key].append(word)
        return list(tuplesToWords.values())



if __name__ == '__main__':
    # strs = ["eat","tea","tan","ate","nat","bat"]
    # outputs = [['bat'],['nat','tan'],['ate','eat','tea']]
    strs = ["c","c"]
    strs1 = [""]
    print(Solution.groupAnagrams(None,strs))

    # Does not work, intersection does not work on duplicates
        # res = []
        # letterToWord = DefaultDict(lambda: set())
        # visitedWords = set()
        # for word in strs: # create dict
        #     if not word:
        #         if not res:
        #             res.append([""])
        #         else:
        #             res[0].append("")
        #         continue
        #     for letter in word:
        #         letterToWord[letter].add(word)
        # if len(res)==1 and len(res[0]) == len(strs):
        #     return res
        # for word in strs:
        #     if not word:
        #         continue
        #     if word not in visitedWords:
        #         letterSets = [letterToWord[x] for x in word[1:]]
        #         anagrams = list(letterToWord[word[0]].intersection(*letterSets))
        #         res.append(anagrams)
        #         for x in anagrams:
        #             visitedWords.add(x)
        #     else:
        #         continue
        # return res