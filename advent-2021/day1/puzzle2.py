"""
Problem Statement: Assuming a sliding window of length 3, how many measurments are now larger if each measuerment
is a sum of the sliding window?
"""

measurments = []

with open("input", "r") as f:
    """
    Opens the input file and saves it
    """
    for line in f:
        cleaned = int(line.strip('\n'))
        measurments.append(cleaned)

def count_increases_window(measurements):
    """
    This can still be done in O(n) since we have acces to the entire array at once.
    The trick to this is the parameters of the sliding window.
    """
    counter = 0

    for i in range(0,len(measurments)-3):
        window_1 = sum([*measurments[i:i+3]])
        window_2 = sum([*measurments[i+1:i+4]])

        if window_2 > window_1:
            counter+=1
    
    return counter


if __name__ == '__main__':
    print(count_increases_window(measurments))