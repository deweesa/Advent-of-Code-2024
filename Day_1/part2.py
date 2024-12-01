#!/usr/bin/env python3
import sys
import heapq

def main(test_mode):
    if test_mode:
        path = "example.txt"
    else:
        path = "input.txt"

    left, right = [], {}

    with open(path, 'r') as file:
        for line in file:
            pair = line.strip().split(' ')
            left.append(int(pair[0]))
            
            right_num = int(pair[-1])
            if right_num not in right.keys():
                right[right_num] = 1
            else:
                right[right_num] += 1

    sim_score = 0

    for i in range(len(left)):
        if left[i] in right.keys():
            sim_score += right[left[i]] * left[i]

    print("sim_score:", sim_score)

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 1 and sys.argv[1] != "-t":
        print("Wrong flag bucko")
        print("\tI only want -t or nothing")
    elif n > 1 and sys.argv[1] == "-t":
        main(True)
    else:
        main(False)
