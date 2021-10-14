def convert(s, numRows):
    output = ['']*len(s)
    connectorLength = numRows - 2 if numRows - 2 > 0 else 0
    for i in range(len(s)):
        location = divmod(i,numRows)
        print(location)
        output[location[0]*numRows + location[1]] = s[i]
    return str(output)

if __name__ == '__main__':
    input1 = ("PAYPALISHIRING",3)
    input2 = ("PAYPALISHIRING", 4)
    print(convert(*input1))