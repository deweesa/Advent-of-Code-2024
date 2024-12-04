#!/usr/bin/env python3
import sys
import time

def main(test_mode):
    if test_mode:
        path = "example.txt"
    else:
        path = "input.txt"

    result = 0
    mem = ""
    with open(path, 'r') as file:
        for line in file:
            mem += line

    mem = mem.strip()

    start = mem.find("mul(")
    while start != -1:
        print(mem[start:start+4])
        
        start = mem.find("mul(", start + 1)

    print(result)

# Get the result from "mul(a,b)"
def getResult(input):
    start = input.index("(") + 1
    end = input.index(")")

    numbers = input[start:end].split(",")
    numbers = [int(x) for x in numbers]
    return numbers[0] * numbers[1]

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 1 and sys.argv[1] != "-t":
        print("Wrong flag bucko")
        print("\tI only want -t or nothing")
    elif n > 1 and sys.argv[1] == "-t":
        main(True)
    else:
        main(False)
