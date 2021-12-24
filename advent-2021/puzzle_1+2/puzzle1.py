"""
Problem Statement: How many measurements are larger than the previous measurments?
"""

measurments = []

with open("input", "r") as f:
    """
    Opens the input file and saves it
    """
    for line in f:
        cleaned = int(line.strip('\n'))
        measurments.append(cleaned)

def count_increases(measurements):
    """
    First thing that comes to mind is an O(n) search
    """
    counter = 0

    for i in range(len(measurments)):
        if i==0:
            continue
        if measurments[i-1] < measurments[i]:
            counter += 1
    return counter


if __name__ == '__main__':
    print(count_increases(measurments))