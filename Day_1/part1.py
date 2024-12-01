#!/usr/bin/env python3
import sys
import heapq
import time

def main(test_mode):
    start = time.time()
    if test_mode:
        path = "example.txt"
    else:
        path = "input.txt"

    left, right = [], []

    with open(path, 'r') as file:
        for line in file:
            pair = line.strip().split(' ')
            left.append(int(pair[0]))
            right.append(int(pair[-1]))

    left.sort()
    right.sort()

    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    end = time.time()

    print("sum:", sum)
    print("Execution time:", (end-start) * 10**3)

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 1 and sys.argv[1] != "-t":
        print("Wrong flag bucko")
        print("\tI only want -t or nothing")
    elif n > 1 and sys.argv[1] == "-t":
        main(True)
    else:
        main(False)
