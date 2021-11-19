from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closing = [')', ']','}']
        pairs = {')':'(','}':'{',']':'['}
        
        for elem in s:
            if elem in closing and stack:
                firstin = stack.pop()
                if firstin == pairs[elem]:
                    continue
                else:
                    return False
            stack.append(elem)
        if stack:
            return False
        return True






if __name__ == "__main__":
    s = "([)]"
    print(Solution.isValid(None,s))