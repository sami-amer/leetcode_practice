def convert(s, numRows):
    rows = min(numRows, len(s))
    row = 0
    arr = ["" for _ in range(rows)]
    flag = -1 #initialize to down

    for letter in s:
        if row == rows:
            flag = 1 # we want to go up
            row = max(row-2, 0) # go back to first row or connector row
        if row == 0:
            flag = -1
        if flag == 1:
            arr[row] += letter
            row -= 1
        if flag == -1:
            arr[row] += letter
            row += 1
    return "".join(arr)

if __name__ == '__main__':
    input1 = ("PAYPALISHIRING",3)
    input2 = ("PAYPALISHIRING", 4)
    print(convert(*input1))