def reverse(x):
    if x <= -2**31 or x >= 2**31-1: return 0
    if x >=0:
        ans = int(str(x)[::-1])
        if ans >= 2**31-1: return 0
        else: return ans 
    else:
        tmp = abs(x)
        tmp = int(str(tmp)[::-1])

        ans = -1*tmp
        if ans <= -2**31: return 0
        else: return ans

if __name__ == '__main__':
    input1 = -321
    print(reverse(input1))
