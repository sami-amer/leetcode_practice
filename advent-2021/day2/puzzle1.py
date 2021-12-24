"""
Problem Statement: What is the final position of the submarine?
Forward: increases horizontal
Up: DECREASES depth
Down: INCREASES depth
"""
from typing import DefaultDict

moves_tot = DefaultDict(lambda: 0)

with open("advent-2021/day2/input", "r") as f: # our input is doing all of the work
    for line in f:
        move, magnitude = line.strip('\n').split(' ')[0], line.strip('\n').split(' ')[1]
        moves_tot[move] += int(magnitude)

horizontal_pos = moves_tot['forward']
depth_pos = moves_tot['down'] - moves_tot['up']

print(horizontal_pos, depth_pos, horizontal_pos*depth_pos)