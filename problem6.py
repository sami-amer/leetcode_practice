def convert(s, numRows):
    rows, row = min(numRows, len(s)), 0
    arr, flag = ["" for _ in range(rows)], 1

    for letter in s:
        if row == rows:
            flag = -1
            row = max(row-2,0)
        if row == 0:
            flag = 1
        if flag == -1:
            arr[row] += letter
            row -= 1
        if flag == 1:
            arr[row] += letter
            row += 1
    return "".join(arr)

if __name__ == '__main__':
    input1 = ("PAYPALISHIRING",3)
    input2 = ("PAYPALISHIRING", 4)
    print(convert(*input1))