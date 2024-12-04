#!/usr/bin/env python3
import sys
import time

def main(test_mode):
    if test_mode:
        path = "example.txt"
    else:
        path = "input.txt"

    count = 0
    with open(path, 'r') as file:
        for line in file:
            nums = line.strip().split(' ')
            if nums == ['']:
                print("empty")
                continue
            nums = [int(x) for x in nums]

            isAscending, isDescending = sorted(nums) == nums, sorted(nums, reverse=True) == nums

            isSafe = isAscending ^ isDescending
            i = 0
            while isSafe and i < len(nums) - 1:
                diff = nums[i+1] - nums[i]

                if abs(diff) == 0 or abs(diff) > 3:
                    isSafe = False
                elif isAscending and diff < 0: # this is confusing lol
                    isSafe = False
                elif isDescending and diff > 0:
                    isSafe = False

                i += 1

            if isSafe:
                count += 1

            print(nums, isAscending, isDescending, isSafe)
        
    print("count:", count)

"""
    In case you come back for day 2 part two, just know that the sort check won't work for ya. If we can tolerate one bad input. 
    We might actually be able to use the sorted lists to compare how many numbers are out of place when checking if we're strictly 
    increasing or decreasing.
"""
if __name__ == "__main__":
    n = len(sys.argv)
    if n > 1 and sys.argv[1] != "-t":
        print("Wrong flag bucko")
        print("\tI only want -t or nothing")
    elif n > 1 and sys.argv[1] == "-t":
        main(True)
    else:
        main(False)
