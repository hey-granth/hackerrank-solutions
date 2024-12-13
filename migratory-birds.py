#!/bin/python3

import os

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    birdCount = {}
    for i in arr:
        birdCount[i] = birdCount.get(i, 0) + 1

    maximum = max(birdCount.values())
    birds = [bird for bird, count in birdCount.items() if count == maximum]
    return min(birds)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
