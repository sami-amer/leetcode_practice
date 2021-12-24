"""
Problem Statement: What is the final position of the submarine?
Forward increases horizontal by X and depth by AIM times X
Up decreases AIM
Down increases AIM
"""

moves = []

with open('advent-2021/day2/input', 'r') as f:
    for line in f:
        move, magnitude = line.strip('\n').split(' ')[0], line.strip('\n').split(' ')[1]

        moves.append((move,int(magnitude)))

def calculate_position(moves):
    """
    This is more complex than last time, since we need to keep track of AIM
    Can be done in O(n)
    """

    aim = 0
    horizontal_pos = 0
    depth_pos = 0

    for move in moves:
        move_name = move[0]
        move_magnitude = move[1]

        if move_name == 'forward':
            horizontal_pos += move_magnitude
            depth_pos += move_magnitude * aim
        elif move_name == 'up':
            aim -= move_magnitude
        elif move_name == 'down':
            aim += move_magnitude
    return horizontal_pos, depth_pos, horizontal_pos*depth_pos


if __name__ == '__main__':
    print(calculate_position(moves))