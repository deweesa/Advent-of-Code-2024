#!/usr/bin/env python3
import sys
import heapq

def main(test_mode):
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

    heapq.heapify(left)
    heapq.heapify(right)

    sum = 0
    for i in range(len(left)):
        sum += abs(heapq.heappop(left) - heapq.heappop(right))

    print("sum:", sum)

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 1 and sys.argv[1] != "-t":
        print("Wrong flag bucko")
        print("\tI only want -t or nothing")
    elif n > 1 and sys.argv[1] == "-t":
        main(True)
    else:
        main(False)
